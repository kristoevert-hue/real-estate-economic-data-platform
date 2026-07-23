-- ========================================================
-- SQL SKRIPT: ANDMELAO TÄIELIK SKEEM (Star Schema Arhitektuur)
-- ========================================================

-- 1. KUSTUTAME VANAD STRUKTUURID (Garantiiks, et loome puhtalt lehelt)
DROP VIEW IF EXISTS vw_PowerBI_KinnisvaraAnalüüs;
DROP INDEX IF EXISTS idx_sales_date;
DROP INDEX IF EXISTS idx_sales_region;
DROP TABLE IF EXISTS fct_RealEstateSales;
DROP TABLE IF EXISTS dim_Regions;
DROP TABLE IF EXISTS dim_Calendar;

-- 2. LOO KALENDRI DIMENSIOONITABEL (Aegrida ja makroandmed)
CREATE TABLE dim_Calendar (
    Date TEXT PRIMARY KEY,
    Year INTEGER NOT NULL,
    Month INTEGER NOT NULL,
    MonthName TEXT NOT NULL,
    Quarter TEXT NOT NULL,
    Euribor_6m REAL,
    Inflation_pct REAL
);

-- 3. LOO REGIOONIDE DIMENSIOONITABEL (Geograafiline jaotus)
CREATE TABLE dim_Regions (
    RegionID INTEGER PRIMARY KEY AUTOINCREMENT,
    City TEXT NOT NULL,
    SubDistrict TEXT NOT NULL
);

-- 4. LOO KINNISVARATEHINGUTE FAKTITABEL (60 000 põhirida)
CREATE TABLE fct_RealEstateSales (
    TransactionID TEXT PRIMARY KEY,
    OrderDate TEXT NOT NULL,
    RegionID INTEGER NOT NULL,
    Rooms INTEGER NOT NULL,
    SquareMeters REAL NOT NULL,
    PriceEUR REAL NOT NULL,
    FOREIGN KEY (OrderDate) REFERENCES dim_Calendar(Date),
    FOREIGN KEY (RegionID) REFERENCES dim_Regions(RegionID)
);

-- 5. ANDMEBAASI INDEKSID JÕUDLUSE OPTIMEERIMISEKS (Performance)
CREATE INDEX IF NOT EXISTS idx_sales_date ON fct_RealEstateSales(OrderDate);
CREATE INDEX IF NOT EXISTS idx_sales_region ON fct_RealEstateSales(RegionID);

-- 6. ÄRILINE KOONDVAADE POWER BI JAOKS (Reporting View)
CREATE VIEW vw_PowerBI_KinnisvaraAnalüüs AS
SELECT 
    f.TransactionID AS "Tehingu ID",
    f.OrderDate AS "Kuupäev",
    c.Year AS "Aasta",
    c.Month AS "Kuu Number",
    c.MonthName AS "Kuu",
    c.Quarter AS "Kvartal",
    r.City AS "Linn",
    r.SubDistrict AS "Linnaosa",
    f.Rooms AS "Tubade Arv",
    f.SquareMeters AS "Pindala m²",
    f.PriceEUR AS "Tehingu Summa €",
    (f.PriceEUR / f.SquareMeters) AS "Ruutmeetri Hind €",
    c.Euribor_6m AS "Euribor 6M",
    c.Inflation_pct AS "Inflatsioon"
FROM fct_RealEstateSales f
JOIN dim_Calendar c ON f.OrderDate = c.Date
JOIN dim_Regions r ON f.RegionID = r.RegionID;
