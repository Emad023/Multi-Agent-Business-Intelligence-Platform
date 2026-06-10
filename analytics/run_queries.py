import pandas as pd
from database.connection import engine

query = """
SELECT
    ROUND(SUM(sales)::numeric,2) AS total_revenue,
    ROUND(SUM(profit)::numeric,2) AS total_profit
FROM sales_fact
"""

df = pd.read_sql(query, engine)

print(df)