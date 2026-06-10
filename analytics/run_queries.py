import pandas as pd
from database.connection import engine

files = [
    "revenue_analysis.sql",
    "customer_analysis.sql",
    "product_analysis.sql",
    "profitability_analysis.sql"
]

for file in files:

    print(f"\n{'='*50}")
    print(file)
    print(f"{'='*50}")

    with open(
        f"analytics/{file}",
        "r"
    ) as f:

        query = f.read()

    df = pd.read_sql(
        query,
        engine
    )

    print(df.head())