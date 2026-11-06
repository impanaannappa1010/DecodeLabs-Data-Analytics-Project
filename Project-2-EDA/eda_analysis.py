
import pandas as pd

# Project 2: Exploratory Data Analysis

# Creating a sample sales dataset
data = {
    "Order_ID": range(101, 121),
    "Date": [
        "2026-01-05", "2026-01-08", "2026-01-12", "2026-01-15",
        "2026-01-20", "2026-01-25", "2026-02-02", "2026-02-05",
        "2026-02-10", "2026-02-14", "2026-02-18", "2026-02-22",
        "2026-03-01", "2026-03-05", "2026-03-10", "2026-03-15",
        "2026-03-18", "2026-03-22", "2026-03-25", "2026-03-30"
    ],
    "Product": [
        "Laptop", "Mobile", "Tablet", "Laptop", "Headphones",
        "Mobile", "Laptop", "Tablet", "Mobile", "Headphones",
        "Laptop", "Mobile", "Tablet", "Laptop", "Headphones",
        "Mobile", "Laptop", "Tablet", "Mobile", "Laptop"
    ],
    "Region": [
        "South", "North", "East", "West", "South",
        "North", "East", "West", "South", "North",
        "East", "West", "South", "North", "East",
        "West", "South", "North", "East", "West"
    ],
    "Quantity": [
        2, 3, 4, 1, 5, 2, 3, 4, 2, 6,
        2, 3, 5, 2, 4, 3, 2, 5, 3, 20
    ],
    "Unit_Price": [
        50000, 15000, 20000, 50000, 2000,
        15000, 50000, 20000, 15000, 2000,
        50000, 15000, 20000, 50000, 2000,
        15000, 50000, 20000, 15000, 50000
    ]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Sales"] = df["Quantity"] * df["Unit_Price"]

# Display dataset
print("\nORIGINAL SALES DATA")
print(df)

# Basic statistics
print("\nBASIC STATISTICS")
print("Total Orders:", df["Order_ID"].count())
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Median Sales:", df["Sales"].median())

print("\nSALES SUMMARY")
print(df["Sales"].describe())

# Product-wise sales
print("\nPRODUCT-WISE SALES")
print(df.groupby("Product")["Sales"].sum())

# Region-wise sales
print("\nREGION-WISE SALES")
print(df.groupby("Region")["Sales"].sum())

# Monthly sales trend
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()

print("\nMONTHLY SALES TREND")
print(df.groupby("Month")["Sales"].sum())

# Save dataset
df.to_csv("sales_data.csv", index=False)

print("\nSales dataset created successfully!")

# ---------------------------------
# DATA VISUALIZATION
# ---------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# 1. Product-wise Sales Chart
product_sales = df.groupby("Product")["Sales"].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=product_sales, x="Product", y="Sales")
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()

# 2. Monthly Sales Trend
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(8, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# 3. Sales Distribution Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Sales", bins=10, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()

# 4. Outlier Detection using IQR
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]

print("\nOUTLIER ANALYSIS")
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Identified Outliers:")
print(outliers[["Order_ID", "Product", "Sales"]])

# 5. Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Sales")
plt.title("Sales Outlier Detection")
plt.xlabel("Sales Amount")
plt.tight_layout()
plt.savefig("sales_boxplot.png")
plt.show()

print("\nAll graphs created and saved successfully!")
