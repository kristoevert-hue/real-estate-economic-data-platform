import os
import json
import random
from datetime import datetime, timedelta

print("KÄIVITATAKSE PIKAAJALINE SUUREMAHULINE KINNISVARA ANDMETORU (2021-2026)...")

def genereeri_kinnisvara_ja_macro():
    linnad = ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"]
    linnaosad = {
        "Tallinn": ["Kesklinn", "Mustamäe", "Lasnamäe", "Põhja-Tallinn", "Pirita"],
        "Tartu": ["Annelinn", "Kesklinn", "Tammelinn", "Karlova"],
        "Pärnu": ["Kesklinn", "Ranna", "Mai", "Ülejõe"],
        "Narva": ["Kesklinn", "Pähklimäe"],
        "Kuressaare": ["Kesklinn", "Ida-Niidu"]
    }
    
    kinnisvara_list = []
    
    # Genereerime 60 000 tehingut, et 6 aasta peale oleks andmete tihedus ühtlane
    for i in range(1, 60001):
        linn = random.choice(linnad)
        linnaosa = random.choice(linnaosad[linn])
        toad = random.randint(1, 4)
        ruutmeetrid = round(toad * random.uniform(20, 30), 1)
        
        # Kuulutuse kuupäev viimase 6 aasta jooksul (kuni 2190 päeva tagasi)
        paevade_vahe = random.randint(0, 2190)
        tehingu_kuupaev = (datetime.now() - timedelta(days=paevade_vahe))
        aasta = tehingu_kuupaev.year
        kuupaev_str = tehingu_kuupaev.strftime("%Y-%m-%d")
        
        # Hind sõltub linnast ja aastast (simuleerime reaalset hinnatõusu aastate lõikes)
        if aasta == 2021:   kordaja = 0.75
        elif aasta == 2022: kordaja = 0.90
        elif aasta == 2023: kordaja = 0.95
        elif aasta == 2024: kordaja = 1.00
        elif aasta == 2025: kordaja = 1.02
        else:               kordaja = 1.05  # 2026 trend
        
        if linn == "Tallinn":
            ruutmeetri_hind = random.uniform(3000, 4500) * kordaja
        elif linn == "Tartu":
            ruutmeetri_hind = random.uniform(2200, 3200) * kordaja
        else:
            ruutmeetri_hind = random.uniform(1500, 2300) * kordaja
            
        hind = round(ruutmeetrid * ruutmeetri_hind, 0)
        
        kinnisvara_list.append({
            "tehingu_id": f"TX{100000 + i}",
            "kuupaev": kuupaev_str,
            "linn": linn,
            "linnaosa": linnaosa,
            "toad": toad,
            "ruutmeetrid": ruutmeetrid,
            "hind_eur": hind
        })
        
    # Pikendame ka makromajanduslikke näitajaid läbi 6 aasta ajaloo
    andmeladu_pakk = {
        "projekti_nimi": "Kinnisvara ja Majandusandmete Platvorm",
        "loodud_at": str(datetime.now())[:19],
        "macro_indicators": [
            {"aasta": 2021, "euribor_6m": -0.50, "tarbijahinnaindeks_muutus_pct": 4.6},
            {"aasta": 2022, "euribor_6m": 1.50, "tarbijahinnaindeks_muutus_pct": 19.4},
            {"aasta": 2023, "euribor_6m": 3.85, "tarbijahinnaindeks_muutus_pct": 9.2},
            {"aasta": 2024, "euribor_6m": 3.90, "tarbijahinnaindeks_muutus_pct": 4.5},
            {"aasta": 2025, "euribor_6m": 2.85, "tarbijahinnaindeks_muutus_pct": 3.2},
            {"aasta": 2026, "euribor_6m": 2.20, "tarbijahinnaindeks_muutus_pct": 2.5}
        ],
        "kinnisvaraturg": kinnisvara_list
    }
    
    try:
        with open("test_data.json", "w", encoding="utf-8") as f:
            json.dump(andmeladu_pakk, f, indent=4, ensure_ascii=False)
            
        print("\n✅ ANDMETORU ON LAIENDATUD 6 AASTA PEALE!")
        print(f"Uuendatud fail: {os.path.abspath('test_data.json')}")
        print(f"Genereeriti edukalt: {len(kinnisvara_list)} kinnisvara tehingut aastateks 2021-2026.")
        
    except Exception as e:
        print(f"❌ Tõrge andmete salvestamisel: {e}")

if __name__ == "__main__":
    genereeri_kinnisvara_ja_macro()
