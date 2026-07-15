
import pandas as pd
import matplotlib.pyplot as plt

# Load Excel
df = pd.read_excel("sales_data.xlsx")

# Total Sales
df["Total Sales"] = df["Quantity"] * df["Price"]

# Print analysis
print("Total Sales:", df["Total Sales"].sum())
print("Average Sales:", df["Total Sales"].mean())
print("Highest Sale:", df["Total Sales"].max())
print("Lowest Sale:", df["Total Sales"].min())

# -----------------------
# 1. Bar Chart
# -----------------------
plt.figure(figsize=(6,4))
plt.bar(df["Product"], df["Total Sales"])
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.savefig("bar_chart.png")
plt.show()

# -----------------------
# 2. Pie Chart
# -----------------------
category_sales = df.groupby("Category")["Total Sales"].sum()

plt.figure(figsize=(6,6))
plt.pie(category_sales,
        labels=category_sales.index,
        autopct="%1.1f%%")
plt.title("Sales by Category")
plt.savefig("pie_chart.png")
plt.show()

# -----------------------
# 3. Line Chart
# -----------------------
month_sales = df.groupby("Month")["Total Sales"].sum()

plt.figure(figsize=(6,4))
plt.plot(month_sales.index,
         month_sales.values,
         marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.savefig("line_chart.png")
plt.show()

# -----------------------
# 4. Scatter Plot
# -----------------------
plt.figure(figsize=(6,4))
plt.scatter(df["Quantity"], df["Total Sales"])
plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")
plt.savefig("scatter_plot.png")
plt.show()

# -----------------------
# 5. Horizontal Bar Chart
# -----------------------
plt.figure(figsize=(6,4))
plt.barh(df["Product"], df["Total Sales"])
plt.title("Horizontal Sales Chart")
plt.xlabel("Total Sales")
plt.savefig("horizontal_bar.png")
plt.show()