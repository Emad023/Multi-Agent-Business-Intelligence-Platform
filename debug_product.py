import pandas as pd

df = pd.read_csv("data/processed/product_dim.csv")

print("Total rows:", len(df))
print("Unique Product IDs:", df["Product ID"].nunique())

duplicates = df[df.duplicated(subset=["Product ID"], keep=False)]

print("\nDuplicate Product IDs:")
print(duplicates.sort_values("Product ID").head(20))