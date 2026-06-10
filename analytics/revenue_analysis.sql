--  Revenue Overview

SELECT
    ROUND(SUM(sales)::numeric, 2) AS total_revenue,
    ROUND(SUM(profit)::numeric, 2) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales_fact;


--  Monthly Revenue Trend

SELECT
    d.year,
    d.month,
    ROUND(SUM(s.sales)::numeric,2) AS revenue
FROM sales_fact s
JOIN dim_date d
ON s.date_key = d.date_key
GROUP BY d.year,d.month
ORDER BY d.year,d.month;