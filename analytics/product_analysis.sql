--  Top Products

SELECT
    p.product_name,
    ROUND(SUM(s.sales)::numeric,2) AS revenue
FROM sales_fact s
JOIN dim_product p
ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;