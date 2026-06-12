import pandas as pd
from database.connection import engine

def get_monthly_revenue():

    query = """
    SELECT
        d.year,
        d.month,
        ROUND(SUM(f.sales)::numeric,2) AS revenue

    FROM sales_fact f

    JOIN dim_date d
        ON f.date_key = d.date_key

    GROUP BY
        d.year,
        d.month

    ORDER BY
        d.year,
        d.month
    """

    return pd.read_sql(query, engine)