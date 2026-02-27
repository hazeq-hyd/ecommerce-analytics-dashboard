
import streamlit as st
import pandas as pd


df = pd.read_csv("data/cleaned_data.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

st.title("📊 E-Commerce Sales Dashboard")

total_revenue = df["TotalPrice"].sum()
total_orders = df["InvoiceNo"].nunique()
total_customers = df["CustomerID"].nunique()

st.metric("Total Revenue", f"${total_revenue:,.0f}")
st.metric("Total Orders", total_orders)
st.metric("Total Customers", total_customers)

st.subheader("Revenue by Country")
country_rev = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False)
st.bar_chart(country_rev)

# # st.subheader("Monthly Revenue")

# # date_col = [col for col in df.columns if "date" in col.lower()][0]

# # df[date_col] = pd.to_datetime(df[date_col])
# # df["Month"] = df[date_col].dt.to_period("M").astype(str)

# # monthly = df.groupby("Month")["Revenue"].sum().reset_index()

# # st.line_chart(monthly, x="Month", y="Revenue")
# # st.write(df.columns)
# # st.write("Columns in dataset:")
# # st.write(df.columns)



st.write("Columns:", df.columns)

date_col = [col for col in df.columns if "date" in col.lower()][0]
df[date_col] = pd.to_datetime(df[date_col])
df["Month"] = df[date_col].dt.to_period("M").astype(str)

revenue_col = df.select_dtypes(include="number").columns[0]

monthly = df.groupby("Month")[revenue_col].sum().reset_index()

st.line_chart(monthly, x="Month", y=revenue_col)





# import streamlit as st
# import pandas as pd

# st.set_page_config(page_title="Ecommerce Analytics Dashboard", layout="wide")

# st.title("📊 Ecommerce Analytics Dashboard")

# # Load data
# df = pd.read_csv("../data/cleaned_data.csv")

# # ---- IDENTIFY DATE COLUMN ----
# date_col = [col for col in df.columns if "date" in col.lower()][0]
# df[date_col] = pd.to_datetime(df[date_col])

# # ---- CREATE MONTH COLUMN ----
# df["Month"] = df[date_col].dt.to_period("M").astype(str)

# # ---- IDENTIFY REVENUE COLUMN (numeric) ----
# numeric_cols = df.select_dtypes(include="number").columns
# revenue_col = numeric_cols[0]   # If multiple numeric columns, change index if needed

# # ==============================
# # KPI SECTION
# # ==============================

# total_revenue = df[revenue_col].sum()
# total_orders = len(df)
# avg_order_value = df[revenue_col].mean()

# col1, col2, col3 = st.columns(3)

# col1.metric("💰 Total Revenue", f"{total_revenue:,.0f}")
# col2.metric("📦 Total Orders", total_orders)
# col3.metric("📈 Avg Order Value", f"{avg_order_value:,.2f}")

# st.divider()

# # ==============================
# # MONTHLY REVENUE CHART
# # ==============================

# st.subheader("📅 Monthly Revenue")

# monthly = df.groupby("Month")[revenue_col].sum().reset_index()

# st.line_chart(monthly, x="Month", y=revenue_col)

# # ==============================
# # CATEGORY ANALYSIS (if exists)
# # ==============================

# category_cols = [col for col in df.columns if "category" in col.lower()]

# if category_cols:
#     category_col = category_cols[0]
#     st.subheader("🛍 Revenue by Category")
#     category_data = df.groupby(category_col)[revenue_col].sum().reset_index()
#     st.bar_chart(category_data, x=category_col, y=revenue_col)