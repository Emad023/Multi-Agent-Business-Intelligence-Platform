-- Profitability Analysis

SELECT
    p.category,
    ROUND(SUM(s.profit)::numeric,2) AS profit
FROM sales_fact s
JOIN dim_product p
ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY profit DESC;