# 🛒 E-Commerce Sales & Customer Analyzer

## 1. Project Overview

This project analyzes an e-commerce sales dataset using **Python, NumPy, and Pandas**.

The project focuses on:

* Loading and inspecting CSV data
* Creating calculated columns
* Sales and revenue analysis
* Grouping and aggregation
* Sorting data
* Filtering data
* NumPy statistical calculations
* Date and time analysis
* Customer spending analysis
* Customer segmentation
* Combining NumPy and Pandas in a practical project

---

# 2. Libraries Used

```python
import numpy as np
import pandas as pd
```

### NumPy

**NumPy** is used for numerical and statistical operations.

Examples:

```python
np.mean()
np.argmax()
np.argmin()
np.median()
np.std()
np.max()
np.min()
np.where()
```

### Pandas

**Pandas** is used for:

* Reading CSV files
* Working with DataFrames
* Filtering
* Grouping
* Aggregating
* Sorting
* Date manipulation

---

# 3. Loading CSV Data

```python
sales = pd.read_csv("ecommerce_sales.csv")
```

`pd.read_csv()` reads a CSV file and converts it into a Pandas **DataFrame**.

A DataFrame is a two-dimensional table containing rows and columns.

---

# 4. Counting Orders

```python
number_of_order = sales["Order_ID"].count()
```

`count()` counts the non-null values in a Series.

Here, it counts the number of orders.

```python
sales["Order_ID"]
```

selects the `Order_ID` column.

---

# 5. Finding Unique Values Using Python Sets

```python
city = sales["City"]

unique_city = set()

for cities in city:
    unique_city.add(cities)
```

A Python `set` stores **unique values**.

For example:

```python
set(["Butwal", "Kathmandu", "Butwal"])
```

becomes:

```text
{"Butwal", "Kathmandu"}
```

The same concept was used for products.

### Important

Pandas provides a simpler alternative:

```python
sales["City"].unique()
```

However, using a Python `set` in this project provides practice with Python data structures.

---

# 6. Creating a Calculated Column

```python
sales["Total Sales"] = sales["Price"] * sales["Quantity"]
```

This creates a new column.

The calculation is performed **element-wise**:

```text
Price × Quantity = Total Sales
```

For example:

```text
850 × 1 = 850
600 × 2 = 1200
80 × 3 = 240
```

This is an example of **vectorized operation** in Pandas.

Instead of using a loop, Pandas performs the calculation on the entire column.

---

# 7. Calculating Total Revenue

```python
total_revenue = sales["Total Sales"].sum()
```

`sum()` adds all values in the column.

Concept:

```text
Total Revenue = Sum of all Total Sales
```

---

# 8. Calculating Average Order Value

```python
average_order_value = np.mean(sales["Total Sales"]).round(2)
```

`np.mean()` calculates the arithmetic mean.

Formula:

```text
Mean = Sum of values / Number of values
```

`.round(2)` rounds the result to two decimal places.

### Pandas alternative

```python
sales["Total Sales"].mean()
```

Both approaches can produce the same mean.

---

# 9. Finding the Highest Order

```python
higher_order_index = np.argmax(sales["Total Sales"])
```

`np.argmax()` returns the **position/index of the maximum value**.

Suppose:

```text
Total Sales
850
1200
240
```

Then:

```python
np.argmax(...)
```

returns:

```text
1
```

because `1200` is at position 1.

We can then use:

```python
sales.iloc[higher_order_index]
```

to retrieve that row.

---

# 10. Finding the Lowest Order

```python
lower_order_index = np.argmin(sales["Total Sales"])
```

`np.argmin()` returns the position of the minimum value.

Then:

```python
sales.iloc[lower_order_index]
```

retrieves the corresponding row.

---

# 11. `iloc` — Position-Based Indexing

`.iloc` means **integer-location based indexing**.

```python
sales.iloc[0]
```

means:

> Give me the row at position 0.

It works based on **position**, not label.

Example:

```python
revenue_by_city.iloc[0]
```

returns the value at the first position.

---

# 12. Finding the Best-Selling Product

```python
best_selling_product = sales.groupby("Product")["Quantity"].sum()
```

First, the data is grouped by product.

For example:

```text
Laptop       2
Phone        4
Mouse        8
```

Then:

```python
.sort_values(ascending=False)
```

sorts the values from highest to lowest.

```python
best_selling_product = (
    best_selling_product.sort_values(ascending=False).head(1).reset_index()
)
```

### Concepts used

* `groupby()`
* `sum()`
* `sort_values()`
* `head()`
* `reset_index()`

---

# 13. `groupby()`

`groupby()` is one of the most important Pandas concepts used in this project.

Example:

```python
sales.groupby("Product")["Total Sales"].sum()
```

This means:

> Group the rows by Product and calculate total sales for each product.

Conceptually:

```text
Raw Data
   ↓
Group by Product
   ↓
Calculate Sum
   ↓
Revenue for each Product
```

---

# 14. Revenue by Product

```python
revenue_by_product = sales.groupby("Product")["Total Sales"].sum()

revenue_by_product = revenue_by_product.sort_values(ascending=False)
```

This calculates the total revenue generated by each product and sorts it from highest to lowest.

---

# 15. Revenue by City

```python
revenue_by_city = sales.groupby("City")["Total Sales"].sum()

revenue_by_city = revenue_by_city.sort_values(ascending=False)
```

This calculates revenue generated by each city.

---

# 16. Finding the Top City

```python
top_city = revenue_by_city.index[0]
top_city_revenue = revenue_by_city.iloc[0]
```

This demonstrates an important difference.

### `.index`

Returns the **index label**.

```python
revenue_by_city.index[0]
```

→ first city name.

### `.iloc`

Returns the value at a **position**.

```python
revenue_by_city.iloc[0]
```

→ revenue at position 0.

Because the Series was sorted descending, position `0` contains the highest-revenue city.

---

# 17. `index` vs `iloc`

Suppose:

```text
City         Revenue
Butwal       2430
Kathmandu    2220
Lalitpur     1675
Pokhara       995
```

Then:

```python
revenue_by_city.index[0]
```

returns:

```text
Butwal
```

while:

```python
revenue_by_city.iloc[0]
```

returns:

```text
2430
```

### Easy rule

```text
.index → label/name
.iloc  → position
```

---

# 18. Category Analysis

```python
analysis_by_category = (
    sales.groupby("Category")
    .agg({"Total Sales": "sum", "Quantity": "sum", "Rating": "mean"})
    .round(2)
)
```

This performs multiple calculations for each category.

### `agg()`

`agg()` allows different aggregation functions to be applied to different columns.

Here:

```text
Total Sales → sum
Quantity    → sum
Rating      → mean
```

This is much more efficient than calculating everything separately.

---

# 19. Filtering Data with Boolean Conditions

## High-value orders

```python
high_value_order = sales[sales["Total Sales"] > 500]
```

This selects only orders where:

```text
Total Sales > 500
```

### `>`

Means strictly greater than.

If an order is exactly 500:

```python
500 > 500
```

is:

```text
False
```

If you wanted to include 500:

```python
sales["Total Sales"] >= 500
```

would be required.

---

# 20. Highly Rated Orders

```python
high_rating = sales[sales["Rating"] >= 4.5]
```

This filters orders with a rating of at least 4.5.

The important concept here is **Boolean indexing**.

The condition creates a sequence of:

```text
True
False
True
False
...
```

Pandas then keeps only the rows
