# Real Estate & Economic Data Platform 🚀

[Eestikeelne kirjeldus / Estonian Description](#-eesti-keeles) | [English Description](#-english-version)

---

## 🇪🇪 Eesti keeles

See on mastaapne, pikaajaline andmeplatvormi ja ärianalüütika (BI) arendusprojekt. Platvormi eesmärk on koondada, puhastada ja analüüsida mahukaid kinnisvaratehingute andmeid (60 000+ tehingut) ning siduda need reaalajas makromajanduslike näitajatega (Euribor, inflatsioon/tarbijahinnaindeks).

Projekti arhitektuur järgib kaasaegset andmelao (**Data Warehouse**) elutsüklit: andmete genereerimine/kraapimine -> ETL torustik -> Täheskeemil põhinev relatsiooniline SQL andmebaas -> Ärianalüütika vaated ja Power BI dashboardid.

### 🏗️ Projekti Struktuur

```text
real-estate-economic-data-platform/
│
├── 01_data_pipeline/           # Andmete kogumise ja ETL-i kiht
│   ├── macro_scraper.py        # Kinnisvaraturgu ja makronäitajaid simuleeriv mootor
│   ├── etl_load_warehouse.py   # Pythoni ETL-torustik (JSON -> SQLite)
│   └── test_data.json          # Genereeritud toorandmete puhverfail
│
├── 02_data_warehouse/          # Andmelao modelleerimise kiht (SQL)
│   ├── create_warehouse.sql    # Täheskeemi (Star Schema) ja vaadete (View) loomise skript
│   └── analuus_paringud.sql    # SQL-päringud andmelao profileerimiseks ja testimiseks
│
├── 03_database/                # Relatsioonilise andmebaasi kiht
│   └── finants_andmeladu.db    # Töötav relatsiooniline SQL andmebaasifail
│
└── 04_analytics_powerbi/       # Visualiseerimise ja ärianalüütika kiht
    └── (Tulevased Power BI raportid ja DAX mudelid)
```

### 🛠️ Tehtud Tööd & Funktsionaalsus

#### 1. Relatsiooniline SQL Andmebaas (`03_database`)
- Püstitatud töötav relatsiooniline **SQL andmebaas (`finants_andmeladu.db`)**, mis toimib platvormi andmelao tuumana.
- Andmebaas on optimeeritud analüütiliste päringute (OLAP) jaoks ning on täielikult valmis otseühenduseks Power BI-ga läbi vaadete kihi.

#### 2. Andmelao Modelleerimine (`create_warehouse.sql`)
- Disainitud puhas **Täheskeem (Star Schema)**, mis eraldab faktid dimensioonidest:
  - `dim_Calendar` (Aeg, aastad, kuud, kvartalid, Euribor 6M ja Inflatsioon)
  - `dim_Regions` (Geograafiline jaotus: linnad ja linnaosad koos `AUTOINCREMENT` unikaalsete ID-dega)
  - `fct_RealEstateSales` (Faktitabel tehingute hindade ja mahtudega)
- Integreeritud **välisvõtmete (Foreign Keys) piirangud** andmete relatsioonilise terviklikkuse tagamiseks.
- Jõudluse optimeerimiseks loodud **andmebaasi indeksid** (`idx_sales_date`, `idx_sales_region`) kuupäeva- ja regioonitunnustele.
- Loodud spetsiaalne äriline koondvaade **`vw_PowerBI_KinnisvaraAnaluus`**, mis ühendab kõik tabelid ja arvutab dünaamiliselt ruutmeetri hinna.

#### 3. Andmete Simulatsioonimootor (`macro_scraper.py`)
- Genereerib **60 000+ unikaalset kinnisvaratehingut** 6 aasta ulatuses (2021–2026).
- Arvestab Eesti suuremaid linnu (Tallinn, Tartu, Pärnu jne) ja nende linnaosasid.
- Sisaldab dünaamilist matemaatilist mudelit, kus korteri lõpphind arvutatakse ruutmeetrite, tubade arvu ning **aastapõhiste majandustrendide kordajate** alusel.
- Koondab tehinguandmed ja makromajanduslikud näitajad (`macro_indicators`) ühte struktureeritud JSON-pakki.

#### 4. ETL Automatiseerimine (`etl_load_warehouse.py`)
- Täielikult automatiseeritud Pythoni torustik, mis seob koodi ja SQL andmebaasi:
  1. Kontrollib lähtefailide olemasolu.
  2. Püstitab andmelao struktuuri, käivitades SQL-skeemi.
  3. Parsib JSON toorandmed ja eraldab sealt unikaalsed dimensioonid.
  4. Laeb andmed SQL andmebaasi, kasutades ülikiiret `executemany` hulgilaadimist.
  5. Käivitab automaatse andmelao **profiilianalüüsi**, kuvades konsooli esimesed testtulemused otse andmebaasist.

### 🚀 Kuidas Süsteemi Käivitada

1. Liigu torustiku kausta:
   ```bash
   cd 01_data_pipeline
   ```
2. Genereeri toorandmed:
   ```bash
   python macro_scraper.py
   ```
3. Käivita ETL-torustik (loob andmebaasi ja laeb andmed):
   ```bash
   python etl_load_warehouse.py
   ```

---

## 🇬🇧 English Version

This is a large-scale, long-term data platform and Business Intelligence (BI) development project. The platform aims to aggregate, clean, and analyze voluminous real estate transaction data (60,000+ records) and correlate them with real-time macroeconomic indicators (Euribor 6M, inflation/CPI).

The platform architecture follows a modern **Data Warehouse** lifecycle: Data Generation/Scraping -> ETL Pipeline -> Star Schema Relational SQL Database -> Analytics Views and Power BI Dashboards.

### 🏗️ Project Structure

```text
real-estate-economic-data-platform/
│
├── 01_data_pipeline/           # Data ingestion & ETL layer
│   ├── macro_scraper.py        # Real estate & macro indicators simulation engine
│   ├── etl_load_warehouse.py   # Python ETL pipeline (JSON -> SQLite)
│   └── test_data.json          # Staging JSON file for raw data
│
├── 02_data_warehouse/          # Data warehouse modeling layer (SQL)
│   ├── create_warehouse.sql    # Star Schema & Reporting View creation script
│   └── analuus_paringud.sql    # SQL queries for data profiling and testing
│
├── 03_database/                # Relational database layer
│   └── finants_andmeladu.db    # Live relational SQL database file
│
└── 04_analytics_powerbi/       # Visualization & Business Intelligence layer
    └── (Future Power BI reports and DAX models)
```

### 🛠️ Features & Implementation Progress

#### 1. Relational SQL Database (`03_database`)
- Deployed a fully functional relational **SQL database (`finants_andmeladu.db`)** serving as the core Data Warehouse.
- Optimized for analytical queries (OLAP processing) and fully prepared for live Power BI connection via the semantic views layer.

#### 2. Data Warehouse Modeling (`create_warehouse.sql`)
- Designed a robust **Star Schema** architectural pattern separating facts and dimensions:
  - `dim_Calendar` (Time dimension handling dates, years, months, quarters, Euribor 6M, and inflation)
  - `dim_Regions` (Geographical dimension mapping cities and sub-districts with `AUTOINCREMENT` primary keys)
  - `fct_RealEstateSales` (Centralized fact table containing quantitative transaction metrics)
- Enforced **Foreign Key constraints** to guarantee strict relational data integrity across tables.
- Built **database indexes** (`idx_sales_date`, `idx_sales_region`) on critical lookup columns to optimize query execution plans.
- Constructed a tailored reporting view **`vw_PowerBI_KinnisvaraAnaluus`** that joins the schema and dynamically calculates metrics like price per square meter.

#### 3. Data Simulation Engine (`macro_scraper.py`)
- Generates **60,000+ realistic real estate transactions** spanning a 6-year horizon (2021–2026).
- Supports major Estonian cities (Tallinn, Tartu, Pärnu, etc.) and their respective sub-districts.
- Embeds a mathematical trend model where final asset prices fluctuate based on square meters, room counts, and **annual macroeconomic trend multipliers**.
- Bundles operational and macroeconomic data (`macro_indicators`) into a single structured JSON payload.

#### 4. ETL Automation Pipeline (`etl_load_warehouse.py`)
- Automated end-to-end Python script tying files to the live SQL database:
  1. Validates the existence of dependent file paths.
  2. Builds the warehouse structure by executing the external SQL schema.
  3. Parses the raw JSON payload and extracts unique dimensions dynamically.
  4. Ingests data using highly efficient bulk loading methods (`executemany`).
  5. Runs automated **data profiling** directly against the SQL database, outputting results to the console.

### 🚀 How to Run the Platform

1. Navigate to the pipeline directory:
   ```bash
   cd 01_data_pipeline
   ```
2. Run the simulation engine to generate data:
   ```bash
   python macro_scraper.py
   ```
3. Run the ETL script to provision the warehouse and load data:
   ```bash
   python etl_load_warehouse.py
   ```

---

## 📈 Project Roadmap (Next Steps)

- [ ] **Power BI Integration:** Connect the `03_database/finants_andmeladu.db` view to Power BI.
- [ ] **DAX Metrics:** Author semantic models tracking average price trends, Year-over-Year (YoY) growth, and Euribor correlation.
- [ ] **Dashboard Design:** Build interactive visualization sheets mapping market dynamics.
- [ ] **Production-grade APIs:** Swap simulated macro metrics with live API feeds from Eesti Pank (Bank of Estonia) or Eurostat.
