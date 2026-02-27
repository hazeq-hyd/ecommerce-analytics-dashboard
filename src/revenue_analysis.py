import pandas as pd

df = pd.read_csv("../data/cleaned_data.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

monthly = df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalPrice"].sum()

print(monthly)