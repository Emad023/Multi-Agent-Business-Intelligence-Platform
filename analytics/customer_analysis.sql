-- Customer Analysis

SELECT
    c.segment,
    COUNT(DISTINCT c.customer_id) AS customers,
    ROUND(SUM(s.sales)::numeric,2) AS revenue
FROM sales_fact s
JOIN dim_customer c
ON s.customer_id = c.customer_id
GROUP BY c.segment
ORDER BY revenue DESC;