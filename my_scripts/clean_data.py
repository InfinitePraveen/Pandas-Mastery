"""Simple script to clean data"""

import pandas as pd

# Load data
df = pd.read_csv("../data/sales.csv")

print("Before cleaning:")
print(f"Rows: {len(df)}")
print(f"Missing values: {df.isnull().sum().sum()}")

# Clean
df_clean = df.dropna()
df_clean["total"] = df_clean["quantity"] * df_clean["price"]

print("\nAfter cleaning:")
print(f"Rows: {len(df_clean)}")
print(f"Missing values: {df_clean.isnull().sum().sum()}")

# Save cleaned data
df_clean.to_csv("../data/cleaned_sales.csv", index=False)
print("\nSaved cleaned data to 'cleaned_sales.csv'")
