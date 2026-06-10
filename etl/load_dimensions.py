import pandas as pd
from database.connection import engine

# Read files
customer_dim = pd.read_csv(
    "data/processed/customer_dim.csv"
)

product_dim = pd.read_csv(
    "data/processed/product_dim.csv"
)

region_dim = pd.read_csv(
    "data/processed/region_dim.csv"
)

date_dim = pd.read_csv(
    "data/processed/date_dim.csv"
)

sales_fact = pd.read_csv(
    "data/processed/sales_fact.csv"
)

# Rename customer columns
customer_dim.columns = [
    "customer_id",
    "customer_name",
    "segment"
]

# Rename product columns
product_dim.columns = [
    "product_id",
    "category",
    "sub_category",
    "product_name"
]

# Rename region columns
region_dim.columns = [
    "country",
    "state",
    "city",
    "postal_code",
    "region"
]

# Load dimensions
customer_dim.to_sql(
    "dim_customer",
    engine,
    if_exists="append",
    index=False
)

product_dim.to_sql(
    "dim_product",
    engine,
    if_exists="append",
    index=False
)

region_dim.to_sql(
    "dim_region",
    engine,
    if_exists="append",
    index=False
)

date_dim.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)

sales_fact.to_sql(
    "sales_fact",
    engine,
    if_exists="append",
    index=False
)

print("All tables loaded successfully!")