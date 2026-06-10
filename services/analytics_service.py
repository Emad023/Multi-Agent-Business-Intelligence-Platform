import pandas as pd
from database.connection import engine


def run_sql_file(file_path):

    with open(file_path, "r") as f:
        query = f.read()

    return pd.read_sql(query, engine)


def get_revenue_metrics():
    return run_sql_file(
        "analytics/revenue_analysis.sql"
    )


def get_customer_metrics():
    return run_sql_file(
        "analytics/customer_analysis.sql"
    )


def get_product_metrics():
    return run_sql_file(
        "analytics/product_analysis.sql"
    )


def get_profit_metrics():
    return run_sql_file(
        "analytics/profitability_analysis.sql"
    )