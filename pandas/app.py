import pandas as pd


# Read data from a CSV file into a DataFrame
# df = pd.read_csv("pandas\sales_data.csv",encoding="utf-8")
# df = pd.read_excel("pandas\Sample_Superstore.xlsx",engine="openpyxl")
df = pd.read_json("pandas\sample_Data.json")
print(df)