# 🏢 Riiklik Reaalajas Kinnisvara- ja Majandusanalüüsi Platvorm (500-Tunnine Suurprojekt)
# Real Estate Market and Macroeconomic Data Platform (500-Hour Enterprise Project)

---

## 🇪🇪 EESTI KEELES

Otsast lõpuni (*End-to-End*) suuremahuline andmeplatvormi ja ärianalüüsi (BI) projekt, mis kraabib, puhastab, struktureerib ja visualiseerib reaalajas Eesti kinnisvaraturu dünaamikat kõrvuti globaalsete makromajanduslike näitajatega (Euribor, inflatsioon). Projekt on disainitud reaalajas toimivaks andmelao lahenduseks.

### 📂 Projekti Kaustastruktuur (Repository Structure)
Koodibaas on jaotatud puhtalt neljaks arenduskeskkonnaks:
* **`01_data_pipeline/`** – Pythoni andmetorud, andmekorjajad (Scrapers) ja kohalikud genereerimismootorid.
* **`02_data_warehouse/`** – SQL andmelao arhitektuuri skriptid, tabelid ja vaated.
* **`03_database/`** – Kohalik relatsiooniline andmebaas arenduseks.
* **`04_analytics_powerbi/`** – Tulemuslikud Power BI dashboardid ja Time Intelligence mudelid.

---

### 🛠️ 1. NÄDAL: Andmetoru vundament ja 6 aasta suurandmete genereerimine
Esimesel nädalal ehitati üles pommikindel andmete genereerimise ja failisüsteemi kirjutamise pipeline (`01_data_pipeline/macro_scraper.py`), mis simuleerib kontrollitud ja äriloogikale vastavat finants- ja kinnisvaraturgu.

* **Andmemaht:** Genereeriti täpselt **60 000 unikaalset kinnisvaratehingut** ja laeti need kohalikku mällu ühtseks JSON-andmepakiks `test_data.json`.
* **Ajaline ulatus:** Andmestik katab katkematu **6 aasta pikkuse ajaloo (2021–2026)**, võimaldades tulevikus ehitada edasijõudnud *Time Intelligence* mõõdikuid.
* **Äriloogika integreerimine:**
  * Simuleeriti reaalset majandustsüklit: 2021. aasta Covidi-järgne buum ja negatiivne Euribor (`-0.50%`), 2022. aasta ränk inflatsioonilaine (`19.4%`) ning turgude stabiliseerumine aastatel 2025–2026.
  * Tehingud jaotati dünaamiliselt viie Eesti linna vahel (Tallinn, Tartu, Pärnu, Narva, Kuressaare) koos spetsiifiliste linnaosade ja unikaalsete ruutmeetri baashindadega, mis peegeldavad reaalset turuseisu.

---

## 🇬🇧 IN ENGLISH

An end-to-end enterprise data platform designed to scrape, process, and visualize real estate market dynamics alongside macroeconomic indicators (Euribor, Inflation). 

### 📂 Repository Directory Structure
* **`01_data_pipeline/`** – Python data pipelines, ingestion scripts, and local generation engines.
* **`02_data_warehouse/`** – SQL data warehouse schemas, DDL scripts, and staging views.
* **`03_database/`** – Relational database instance.
* **`04_analytics_powerbi/`** – Production-grade Power BI report files.

---

### 🛠️ WEEK 1: Pipeline Foundation & 6-Year Bulk Data Generation
During the first week, a robust local data generation pipeline (`01_data_pipeline/macro_scraper.py`) was engineered to simulate a validated, corporate financial and housing data infrastructure.

* **Data Volume:** Systematically generated **60,000 unique real estate transactions**, outputting them natively into a structured JSON payload named `test_data.json`.
* **Temporal Horizon:** The dataset spans a continuous **6-year historical timeline (2021–2026)** to accommodate complex macro time intelligence modeling.
* **Macroeconomic Realism:**
  * Simulated authentic market cycles: The 2021 post-Covid boom with a negative Euribor (`-0.50%`), the massive 2022 inflation spike (`19.4%`), and market stabilization toward 2025–2026.
  * Distributed transactional weights dynamically across 5 regional clusters (Tallinn, Tartu, Pärnu, Narva, Kuressaare) complete with sub-district constraints and price-per-square-meter scaling factors.
