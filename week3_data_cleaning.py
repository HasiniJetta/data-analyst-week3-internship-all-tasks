import pandas as pd

# Read the original dataset
df = pd.read_csv("data.csv")

# Display the original date values
print("ORIGINAL DATE VALUES:")
print(df["Date"])

# Remove extra single quotes and spaces from date values
df["Date"] = df["Date"].astype("string").str.strip().str.strip("'")

# Convert dates into a consistent date format
df["Date"] = pd.to_datetime(
    df["Date"],
    format="mixed",
    errors="coerce"
)

# Display the cleaned date values
print("\nCLEANED DATE VALUES:")
print(df["Date"])

# Check for missing dates
print("\nMISSING DATES:")
print(df["Date"].isnull().sum())