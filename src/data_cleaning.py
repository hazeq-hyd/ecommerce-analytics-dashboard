import pandas as pd

df = pd.read_csv("data/ecommerce_data.csv", encoding="ISO-8859-1")

# remove missing customer IDs
df = df.dropna(subset=["CustomerID"])

# convert date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df.dropna(subset=["InvoiceDate"])

# create total price column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# remove negative quantities (returns)
df = df[df["Quantity"] > 0]

df.to_csv("data/cleaned_data.csv", index=False)

print("Data cleaned successfully!")