# DecodeLabs – Data Analytics Internship

## Project 1: Data Cleaning and Preparation

### 1. Introduction
Data cleaning is an important step in data analytics. It involves identifying and correcting errors, handling missing values, removing duplicate records, and standardizing data formats.

This project demonstrates the process of cleaning and preparing a sample dataset using Python.

### 2. Objective
The main objectives of this project are:
- Identify missing values.
- Handle missing data.
- Remove duplicate records.
- Correct date formats.
- Standardize text values.
- Validate the final cleaned dataset.

### 3. Tools and Technologies Used
- Programming Language: Python
- Library: Pandas
- Code Editor: Visual Studio Code
- File Format: CSV

### 4. Dataset Description
A sample dataset was created for practice because a separate dataset was not provided.

The dataset contains five columns:
- Order_ID
- City
- Date
- Quantity
- Value

The original dataset contains 6 records.

### 5. Data Cleaning Process

**A. Identifying Missing Values**

Missing values were identified using Pandas `isnull()`.

**B. Handling Missing Values**

- Missing City values were replaced with "Unknown".
- Missing Quantity values were replaced with the median.
- Missing Value entries were replaced with the median.

**C. Standardizing City Names**

Extra spaces were removed and city names were converted into title case.

**D. Correcting Date Formats**

Different date formats were converted into the standard YYYY-MM-DD format. Invalid dates were identified.

**E. Removing Duplicates**

Duplicate Order_ID records were removed, keeping the first occurrence.

**F. Handling Invalid Dates**

The record with an invalid date was removed because its correct date could not be determined.

### 6. Final Results

- Original records: 6
- Final records: 4
- Original columns: 5
- Duplicate Order IDs after cleaning: 0
- Missing values after cleaning: 0
- Final dataset shape: 4 rows × 5 columns

### 7. Output
The cleaned dataset was saved as `cleaned_data.csv`.

### 8. Conclusion
This project helped demonstrate the importance of data cleaning and preparation in data analytics. Using Python and Pandas, missing values were handled, duplicate records were removed, city names were standardized, and date formats were corrected.

The final dataset is cleaner and ready for further analysis.