import numpy as np
import pandas as pd

sales = pd.read_csv("E-Commerce-Sales-and-Customer-Analyzer/ecommerce_sales.csv")
# number of orders
number_of_order = sales["Order_ID"].count()
# Unique cities
city = sales["City"]
unique_city = set()
for cities in city:
    unique_city.add(cities)
# Unique products
product = sales["Product"]
unique_product = set()
for products in product:
    unique_product.add(products)
# total sale
sales["Total Sales"] = sales["Price"] * sales["Quantity"]
# total revenue
total_revenue = sales["Total Sales"].sum()
# average order value
average_order_value = np.mean(sales["Total Sales"]).round(2)
# Highest order value
higher_order_index = np.argmax(sales["Total Sales"])
print("Highest order :", sales.iloc[higher_order_index]["Total Sales"])
# lowest order value
lower_order_index = np.argmin(sales["Total Sales"])
print("Lowest order :", sales.iloc[lower_order_index]["Total Sales"])
# total product sold
total_product_sold = (
    sales.groupby("Product")["Quantity"].sum().idxmax()
)  # idmax tells us the highest product sold
# Revenue by Product
revenue_by_product = sales.groupby("Product")["Total Sales"].sum()
revenue_by_product = revenue_by_product.sort_values(ascending=False)
# Revenue by City
revenue_by_city = sales.groupby("City")["Total Sales"].sum()
revenue_by_city = revenue_by_city.sort_values(ascending=False)
top_city = revenue_by_city.index[0]
top_city_revenue = revenue_by_city.iloc[0]
# Category Analysis
analysis_by_category = (
    sales.groupby("Category")
    .agg({"Total Sales": "sum", "Quantity": "sum", "Rating": "mean"})
    .round(2)
)
# print(analysis_by_category)
high_value_order = sales[sales["Total Sales"] > 500]
# print(high_value_order[["Order_ID", "Customer", "Product", "Total Sales"]])
# Highly rated products
high_rating = sales[sales["Rating"] >= 4.5]
# print(high_rating[["Customer", "Product", "Rating", "City"]])
sales_array = sales["Total Sales"].to_numpy()
best_selling_product = sales.groupby("Product")["Quantity"].sum()
best_selling_product = (
    best_selling_product.sort_values(ascending=False).head(1).reset_index()
)
# average = np.mean(sales_array)
# medin = np.median(sales_array)
# sd = np.std(sales_array)
# higghest = np.max(sales_array)
# lowest = np.min(sales_array)
# print(higghest, lowest, average, sd, medin)
sales["Date"] = pd.to_datetime(sales["Date"])
sales["Month"] = sales["Date"].dt.month
sales["Month_name"] = sales["Date"].dt.month_name()
revenue_by_month = sales.groupby("Month_name")["Total Sales"].sum().reset_index()
# Customer Analysis
total_spending_by_customer = sales.groupby("Customer")["Total Sales"].sum()
total_spending_by_customer = total_spending_by_customer.sort_values(ascending=False)
top_customer = total_spending_by_customer.index[0]
top_customer_revenue = total_spending_by_customer.iloc[0]
customer_segment = np.where(
    total_spending_by_customer >= 1000,
    "VIP",
    (np.where(total_spending_by_customer >= 500, "Regular", "New")),
)
print(f"""\n==================================================
          E-COMMERCE SALES ANALYSIS
==================================================\n
Total orders :{number_of_order}\n
Average order value : {average_order_value}""")
print("""--------------------------------------------------
Unique Products
--------------------------------------------------""")
for products in unique_product:
    print(f"{products}")
print("""--------------------------------------------------
Unique Cities
--------------------------------------------------""")
for city in unique_city:
    print(f"{city}")
print(f"""--------------------------------------------------
BEST SELLING PRODUCT
--------------------------------------------------
{best_selling_product.to_string(index=False)}""")
print("""--------------------------------------------------
TOP REVENUE PRODUCTS
--------------------------------------------------""")
for products, revenue in revenue_by_product.items():
    print(f"{products} : RS.{revenue}")
print("""--------------------------------------------------
CITY ANALYSIS
--------------------------------------------------""")
for cities, revenue in revenue_by_city.items():
    print(f"{cities} : RS.{revenue}\n")
print(f"Top City : {top_city} , Revenue : RS.{top_city_revenue}")
print(f"""--------------------------------------------------
CUSTOMER ANALYSIS
--------------------------------------------------
\nTop Customer : {top_customer} , Revenue : RS.{top_customer_revenue}""")
print(f"""--------------------------------------------------
MONTHLY REVENUE
--------------------------------------------------\n
{revenue_by_month.to_string(index=False)}""")
print("""--------------------------------------------------
CUSTOMER SEGMENTS
--------------------------------------------------""")
for segment, customer in zip(customer_segment, total_spending_by_customer.index):
    print(f"{customer} : {segment} ")
