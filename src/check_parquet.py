import pandas as pd

# Load Parquet file
df = pd.read_parquet("C:/Users/jakin/Desktop/KIAM program/insurance-risk-analytics/data/insurance_data.parquet")

# Display basic info
print("Data Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())