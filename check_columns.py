import pandas as pd

files = [
    "customer_dim.csv",
    "product_dim.csv",
    "region_dim.csv",
    "date_dim.csv",
    "sales_fact.csv"
]

for file in files:
    df = pd.read_csv(f"data/processed/{file}")
    print(f"\n{file}")
    print(df.columns.tolist())