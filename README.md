# Real Estate & Economic Data Platform 🚀

This is a large-scale, long-term Data Platform and Business Intelligence (BI) development project. The platform is designed to aggregate, clean, and analyze comprehensive real estate transaction data (60,000+ transactions) and correlate them with real-time macroeconomic indicators (6-Month Euribor, Inflation/CPI) and AI-powered predictive capabilities.

The platform architecture follows a modern **Data Warehouse (DWH)** lifecycle: Data Generation/Scraping -> ETL Pipeline -> Relational SQL Database (Star Schema) -> Machine Learning Predictive Model -> Analytical Reporting Views & Power BI Dashboards.

---

## 🏗️ Project Structure

The project directory is structured into logical layers corresponding to the data processing steps:

```text
real-estate-economic-data-platform/
│
├── 01_data_pipeline/           # Data Ingestion, ETL & AI Layer
│   ├── macro_scraper.py        # Core data generation engine (Simulates market & macro trends)
│   ├── etl_load_warehouse.py   # Python-based ETL pipeline (JSON to SQLite)
│   ├── predict_prices.py       # Interactive AI & Machine Learning price prediction module
│   ├── kinnisvara_mudel.pki    # Serialized and optimized AI model file
│   └── test_data.json          # Buffered raw data file (JSON format)
│
├── 02_data_warehouse/          # Data Warehouse Modeling Layer (SQL)
│   ├── create_warehouse.sql    # DWH schema definition (Star Schema & Views)
│   └── analuus_paringud.sql    # Analytical SQL queries for profiling and testing
│
├── 03_database/                # Relational Database Storage Layer
│   └── finants_andmeladu.db    # Live relational SQL database file
│
└── 04_analytics_powerbi/       # Business Intelligence & Visualization Layer
    └── (Upcoming Power BI reports and DAX models)
```

---

## 🛠️ Features & Implementation Details

### 1. Interactive AI & Machine Learning (`predict_prices.py`)
- **Model Architecture:** Utilizes a **Random Forest Regressor** machine learning algorithm trained on the massive simulated dataset.
- **Feature Engineering:** Implements *One-Hot Encoding* to transform categorical text data (cities, sub-districts) into machine-readable mathematical formats.
- **High Accuracy:** The model achieves a stellar **93.37% confidence score ($R^2$ score)**, providing property evaluations with a highly minimized margin of error.
- **Feature Importance Breakdown:**
  - Property Size (Square Meters): **61.9% impact** on final valuation.
  - Location (Tallinn): **23.9% impact**.
- **Interactive CLI Interface:** A user-friendly terminal interface enabling users to inputs custom variables (City, Sub-district, Rooms, $m^2$, Target Year) and instantly receive an AI-driven market value forecast.
- **Model Efficiency:** Saves the trained state as `kinnisvara_mudel.pki`, bypassing retraining on subsequent launches for immediate execution.

### 2. Relational SQL Database & Prediction Logging (`03_database`)
- Built a fully operational relational **SQL database (`finants_andmeladu.db`)** executing OLAP analytical workloads.
- **Prediction Auditing Layer (`fct_PredictionLogs`):** Built an automated pipeline that logs every user interactive forecast. Every user-queried variable and AI-calculated valuation is captured alongside a live `Timestamp`, creating a data log to analyze consumer behavior and market demands over time.

### 3. Data Warehouse Modeling (`create_warehouse.sql`)
- Implemented a standard **Star Schema** architecture to separate facts from dimensions, optimizing query performance for reporting tools:
  - `dim_Calendar` (Time dimensions: Year, Month, Month Name, Quarter, integrated with 6M Euribor and Inflation rates)
  - `dim_Regions` (Geographical indexing: Cities and Sub-districts utilizing unique `AUTOINCREMENT` keys)
  - `fct_RealEstateSales` (Core transactional fact table aggregating prices, volumes, and foreign key relationships)
- Enforces strict **Foreign Key Constraints** to ensure relational data integrity across all dimensions.
- Performance optimization achieved via relational **Database Indexes** (`idx_sales_date`, `idx_sales_region`) on critical lookup columns.
- Constructed a central business reporting view **`vw_PowerBI_KinnisvaraAnaluus`** tailored specifically for DirectQuery/Import connections into BI software.

### 4. Data Generation & Simulation Engine (`macro_scraper.py`)
- Generates **60,000+ realistic real estate transactions** spanning a 6-year horizon (2021–2026).
- Dynamically weights values across major Estonian hubs (Tallinn, Tartu, Pärnu, Narva, Kuressaare) and their respective sub-districts.
- Integrates a mathematical trend model factoring in property scaling benchmarks alongside **annual macroeconomic multipliers**.

### 5. ETL Pipeline Automation (`etl_load_warehouse.py`)
- A fully automated Python data orchestration pipeline that bridges code scripts and database persistence:
  1. Validates structural file system prerequisites.
  2. Provisions the DWH framework by executing database initialization SQL scripts.
  3. Parses raw JSON buffers and dynamically populates dimensions.
  4. Streams transactions directly into SQL schemas utilizing low-latency `executemany` batch loading processes.
  5. Runs automated profiling scripts upon completion to verify operational reliability.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have **Python 3.x** installed along with machine learning frameworks (e.g., `scikit-learn` and `pandas`). To inspect database schemas directly, **DB Browser for SQLite** is highly recommended.

### How to Run the Infrastructure
Open your terminal inside the project root directory and execute the following deployment sequence:

1. Navigate to the pipeline package:
   ```bash
   cd 01_data_pipeline
   ```

2. Generate raw source materials:
   ```bash
   python macro_scraper.py
   ```

3. Deploy database tables and trigger the ETL engine:
   ```bash
   python etl_load_warehouse.py
   ```

4. Launch the interactive Artificial Intelligence forecasting application:
   ```bash
   python predict_prices.py
   ```

---

## 📈 Project Roadmap

With core database infrastructure, extraction pipelines, and machine learning models fully validated, development moves into the analytics and enhancement phase:
- [ ] **Power BI Integration:** Establish data connections linking `03_database/finants_andmeladu.db` analytical views and user log frameworks directly into the reporting layer.
- [ ] **DAX Metrics Formulation:** Engineer calculations measuring dynamic square meter price fluctuations, Year-over-Year (YoY) velocity, and macroeconomic interest rate correlations.
- [ ] **Interactive Dashboard Prototyping:** Build charts to capture broader real estate trends alongside consumer forecasting behaviors.
- [ ] **Live API Connectors:** Transition from simulated parameters to automated web scrapers pulling raw numbers directly from official central banking or statistical APIs.

