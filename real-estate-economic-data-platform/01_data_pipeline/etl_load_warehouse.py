import os
import json
import sqlite3
from datetime import datetime, timedelta

print("KÄIVITATAKSE ANDMELAO ETL TORU (WEEK 2)...")

# Määrame täpsed teed sinu kaustastruktuuri põhjal
DB_PATH = "../03_database/finants_andmeladu.db"
JSON_PATH = "test_data.json"
SQL_SKEEM_PATH = "../02_data_warehouse/create_warehouse.sql"

def loe_sql_fail(failitee):
    with open(failitee, 'r', encoding='utf-8') as f:
        return f.read()

def run_etl():
    # 1. Kontrollime, kas andmefail on olemas
    if not os.path.exists(JSON_PATH):
        print(f"❌ Tõrge: Toorandmete faili '{JSON_PATH}' ei leitud! Käivita esmalt macro_scraper.py")
        return
        
    # 2. Ühendame andmebaasiga (loob faili automaatselt, kui seda pole)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print(" -> Luuakse andmelao tabelite struktuurid, indeksid ja vaated...")
    sql_skeem = loe_sql_fail(SQL_SKEEM_PATH)
    cursor.executescript(sql_skeem)
    conn.commit()
    
    # 3. Loeme JSON-andmed sisse
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # 4. TÄIDAME DIM_CALENDAR (Aegrida 2021-2026 koos makronäitajatega)
    print(" -> Täidetakse ajadimensioon (dim_Calendar)...")
    macro_dict = {m['aasta']: m for m in data['macro_indicators']}
    
    alg_kp = datetime(2021, 1, 1)
    kalender_rows = []
    
    # Loome iga päeva jaoks rea läbi 6 aasta ajaloo (2192 päeva koos liigaastaga)
    for d in range(2192):
        jooksev_kp = alg_kp + timedelta(days=d)
        kp_str = jooksev_kp.strftime("%Y-%m-%d")
        aasta = jooksev_kp.year
        
        macro = macro_dict.get(aasta, {"euribor_6m": 0, "tarbijahinnaindeks_muutus_pct": 0})
        
        kalender_rows.append((
            kp_str, aasta, jooksev_kp.month, 
            jooksev_kp.strftime("%B"), f"Q{(jooksev_kp.month-1)//3 + 1}",
            macro['euribor_6m'], macro['tarbijahinnaindeks_muutus_pct']
        ))
        
    cursor.executemany("INSERT INTO dim_Calendar VALUES (?,?,?,?,?,?,?)", kalender_rows)
    
    # 5. TÄIDAME DIM_REGIONS (Eraldame unikaalsed asukohad)
    print(" -> Täidetakse regioonide dimensioon (dim_Regions)...")
    regioonid_set = set()
    for t in data['kinnisvaraturg']:
        regioonid_set.add((t['linn'], t['linnaosa']))
        
    regioonid_mapping = {}
    for idx, (linn, lo) in enumerate(regioonid_set, 1):
        cursor.execute("INSERT INTO dim_Regions (City, SubDistrict) VALUES (?,?)", (linn, lo))
        regioonid_mapping[(linn, lo)] = idx
        
    # 6. TÄIDAME FCT_REALESTATESALES (Laeme 60 000 tehingut)
    print(f" -> Laetakse {len(data['kinnisvaraturg'])} tehingut faktitabelisse (fct_RealEstateSales)...")
    fakt_rows = []
    for t in data['kinnisvaraturg']:
        reg_id = regioonid_mapping[(t['linn'], t['linnaosa'])]
        fakt_rows.append((
            t['tehingu_id'], t['kuupaev'], reg_id, 
            t['toad'], t['ruutmeetrid'], t['hind_eur']
        ))
        
    cursor.executemany("INSERT INTO fct_RealEstateSales VALUES (?,?,?,?,?,?)", fakt_rows)
    
    # Kinnitame kõik muudatused ja sulgeme ühenduse
    conn.commit()
    conn.close()
    
    print("\n✅ ÕNNESTUS! 2. Nädala ETL toru on edukalt käivitunud!")
    print(f"Andmeladu on püstitatud aadressil: {os.path.abspath(DB_PATH)}")

def test_andmeladu_paringuga():
    print("\n -> Käivitatakse andmelao profiilianalüüs (analuus_paringud.sql)...")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Loeme SQL päringu failist sisse
    with open("../02_data_warehouse/analuus_paringud.sql", "r", encoding="utf-8") as f:
        sql_paring = f.read()
        
    try:
        cursor.execute(sql_paring)
        rows = cursor.fetchall()
        
        print("\n🏆 ANDMELAO TESTPÄRINGU TULEMUSED (Esimesed 5 rida):")
        print(f"{'Aasta':<5} | {'Linn':<11} | {'Tehingud':<8} | {'Kogukäive (€)':<16} | {'Keskmine m² (€)':<15} | {'Euribor':<8} | {'Inflatsioon':<10}")
        print("-" * 90)
        
        for r in rows[:5]:
            print(f"{r[0]:<5} | {r[1]:<11} | {r[2]:<8} | {r[3]:<16,.2f} | {r[4]:<15,.2f} | {r[5]:<8}% | {r[6]:<10}%")
            
    except Exception as e:
        print(f"❌ Tõrge SQL päringu käivitamisel: {e}")
        
    conn.close()

if __name__ == "__main__":
    run_etl()
    test_andmeladu_paringuga()  # Käivitame testimise kohe pärast laadimist

