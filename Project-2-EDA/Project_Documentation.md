# Project 2: Exploratory Data Analysis (EDA)

## 1. Project Overview

This project focuses on Exploratory Data Analysis (EDA) using Python. The purpose is to examine a sales dataset, calculate statistical measures, identify trends, detect outliers, and understand business performance.

**Dataset:** Sample Sales Dataset  
**Tools Used:** Python, Pandas, Matplotlib, Seaborn  
**IDE:** Visual Studio Code

**Note:** This is a sample dataset created for learning and analysis because a separate dataset was not provided by DecodeLabs.

## 2. Project Objectives

- Understand the structure of the sales dataset.
- Calculate basic statistical measures such as mean, median, and count.
- Analyze sales by product and region.
- Identify monthly sales trends.
- Detect unusual values (outliers).
- Present findings through graphs and visualizations.

## 3. Dataset Description

The dataset contains 20 sample sales records.

| Column | Description |
|---|---|
| Order_ID | Unique order identification number |
| Date | Date of the order |
| Product | Product category |
| Region | Sales region |
| Quantity | Number of units sold |
| Unit_Price | Price per unit |
| Sales | Total sales amount |

Sales is calculated using:

**Sales = Quantity × Unit_Price**

## 4. Tools and Technologies

- **Python:** Programming language used for analysis.
- **Pandas:** Used for data handling and statistical calculations.
- **Matplotlib:** Used to create graphs.
- **Seaborn:** Used to create attractive statistical visualizations.
- **VS Code:** Used to write and execute Python code.

## 5. Data Analysis

The dataset was analyzed to understand overall sales performance.

### Basic Statistics

- Total Orders: 20
- Total Sales: ₹22,30,000
- Average Sales: ₹1,11,500
- Median Sales: ₹65,000

The mean is higher than the median because one order has a particularly high sales value.

### Product-wise Sales Analysis

- Laptop: ₹16,00,000
- Mobile: ₹2,40,000
- Tablet: ₹3,60,000
- Headphones: ₹30,000

**Observation:** Laptops generated the highest sales among all product categories.

### Region-wise Sales Analysis

- South: ₹3,40,000
- North: ₹2,87,000
- East: ₹3,83,000
- West: ₹12,20,000

**Observation:** The West region recorded the highest sales.

### Monthly Sales Analysis

- January: ₹3,15,000
- February: ₹4,17,000
- March: ₹14,98,000

**Observation:** March recorded the highest sales. This result is strongly influenced by one unusually large order.

## 6. Data Visualization

Four graphs were created using Matplotlib and Seaborn.

1. **Product-wise Sales:** Compares sales across different product categories.
2. **Monthly Sales:** Shows changes in sales across the months.
3. **Sales Distribution:** Displays how sales values are distributed.
4. **Sales Boxplot:** Helps identify unusual sales values and outliers.

## 7. Outlier Detection

The Interquartile Range (IQR) method was used to identify outliers.

- Q1: ₹41,250
- Q3: ₹1,00,000
- IQR: ₹58,750
- Lower Limit: -₹46,875
- Upper Limit: ₹1,88,125

**Identified Outlier:**

- Order ID: 120
- Product: Laptop
- Sales: ₹10,00,000

**Observation:** Order 120 is above the upper limit and is identified as an outlier. It should be investigated to determine whether it represents a genuine large order or an unusual data entry.

## 8. Key Findings

- Laptops generated the highest product-wise sales.
- The West region had the highest regional sales.
- March recorded the highest monthly sales.
- Order 120 was identified as an unusually high sales value.
- The average sales value was higher than the median because of the outlier.

## 9. Conclusion

This project provided practical experience in Exploratory Data Analysis using Python. Statistical calculations and visualizations helped identify sales patterns, compare product and regional performance, and detect outliers.

The analysis showed how data can support business decisions by highlighting important trends and unusual values.

## 10. Learning Outcomes

Through this project, I learned:

- How to create and analyze a dataset using Pandas.
- How to calculate mean, median, and descriptive statistics.
- How to group and compare sales data.
- How to create graphs using Matplotlib and Seaborn.
- How to identify outliers using the IQR method.
- How to interpret analytical results and communicate findings.