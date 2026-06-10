import pandas as pd
from database.connection import engine

def get_financial_summary():

    query = """
    SELECT
        ROUND(CAST(SUM(sales) AS numeric), 2) AS total_revenue,
        ROUND(CAST(SUM(profit) AS numeric), 2) AS total_profit,
        ROUND(
            CAST(
                (SUM(profit) / NULLIF(SUM(sales), 0)) * 100
                AS numeric
            ),
            2
        ) AS profit_margin
    FROM sales_fact;
    """

    return pd.read_sql(query, engine)