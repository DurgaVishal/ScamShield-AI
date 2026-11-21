import pandas as pd

data_path = "data/raw/SMSSpamCollection.txt"

df = pd.read_csv(
    data_path,
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Basic dataset information
print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Messages:")
print(df.duplicated().sum())

print("\nLabel Distribution:")
print(df["label"].value_counts())


# Data cleaning

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate rows
df_clean = df.drop_duplicates()

# Check dataset after removing duplicates
print("\nDataset shape after cleaning:", df_clean.shape)

print("\nDuplicates removed:", df.shape[0] - df_clean.shape[0])

# Save cleaned dataset
import os

os.makedirs("data/processed", exist_ok=True)

df_clean.to_csv("data/processed/sms_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
