-- DÜNAAMILINE TURUANALEES: Kinnisvaratrendid vs Makromajandus (2021-2026)

SELECT 
    c.Year AS "Aasta",
    r.City AS "Linn",
    COUNT(f.TransactionID) AS "Tehingute Arv",
    ROUND(SUM(f.PriceEUR), 2) AS "Kogukäive (€)",
    ROUND(AVG(f.PriceEUR / f.SquareMeters), 2) AS "Keskmine m² Hind (€)",
    c.Euribor_6m AS "Euribor 6M %",
    c.Inflation_pct AS "Inflatsioon %"
FROM fct_RealEstateSales f
JOIN dim_Calendar c ON f.OrderDate = c.Date
JOIN dim_Regions r ON f.RegionID = r.RegionID
GROUP BY c.Year, r.City
ORDER BY c.Year ASC, "Kogukäive (€)" DESC;
