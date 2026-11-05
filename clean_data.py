
import pandas as pd

# Create a sample dataset for practice
data = {
    "Order_ID": [101, 102, 102, 104, 105, 106],
    "City": [" Bangalore ", "mysore", "mysore", "BANGALORE", None, "Hubli"],
    "Date": [
        "2026-10-01",
        "02/10/2026",
        "02/10/2026",
        "2026-10-04",
        "invalid",
        "06/10/2026"
    ],
    "Quantity": [2, 3, None, 5, 4, 2],
    "Value": [500.00, 750.50, 750.50, None, 900.00, 300.00]
}

df = pd.DataFrame(data)

print("ORIGINAL SAMPLE DATA")
print(df)

print("\nDATASET INFORMATION")
print(df.info())

print("\nMISSING VALUES IN EACH COLUMN")
print(df.isnull().sum())

print("\nNUMBER OF DUPLICATE ORDER IDs")
print(df["Order_ID"].duplicated().sum())

# Clean city names
df["City"] = df["City"].str.strip().str.title()

print("\nCITY NAMES AFTER CLEANING")
print(df["City"])

# Handle missing values

df["City"] = df["City"].fillna("Unknown")

df["Quantity"] = df["Quantity"].fillna(
    df["Quantity"].median()
)

df["Value"] = df["Value"].fillna(
    df["Value"].median()
)

print("\nDATA AFTER HANDLING MISSING VALUES")
print(df)

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# Clean date formats correctly

def clean_date(date):
    try:
        return pd.to_datetime(date, format="%Y-%m-%d")
    except (ValueError, TypeError):
        try:
            return pd.to_datetime(date, format="%d/%m/%Y")
        except (ValueError, TypeError):
            return pd.NaT

df["Date"] = df["Date"].apply(clean_date)

print("\nDATES AFTER CLEANING")
print(df["Date"])

# Convert dates to standard format
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

print("\nDATES IN STANDARD FORMAT")
print(df["Date"])

# Remove rows with invalid dates
df = df.dropna(subset=["Date"]).copy()

# Remove duplicate Order IDs
df = df.drop_duplicates(subset=["Order_ID"], keep="first")

print("\nFINAL CLEANED DATA")
print(df)

print("\nDUPLICATE ORDER IDs AFTER CLEANING")
print(df["Order_ID"].duplicated().sum())

# Final data quality check

print("\nMISSING VALUES IN FINAL DATA")
print(df.isnull().sum())

print("\nFINAL DATASET SHAPE")
print(df.shape)

# Save the cleaned dataset
df.to_csv("cleaned_data.csv", index=False, float_format="%.2f")

print("\nCleaned dataset saved successfully!")

# Verify date formatting

print("\nINVALID DATES AFTER CLEANING")
print(df["Date"].isna().sum())

print("\nDATE FORMAT CHECK")
print(df["Date"].apply(
    lambda x: len(x) == 10 and x[4] == "-" and x[7] == "-"
).all())
