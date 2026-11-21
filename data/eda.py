import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/processed/sms_cleaned.csv")

# Dataset overview
print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check spam and ham counts
print("\nLabel Distribution:")
print(df["label"].value_counts())

import matplotlib.pyplot as plt

# Count ham and spam messages
label_counts = df["label"].value_counts()

# Create bar chart
label_counts.plot(kind="bar", color=["skyblue", "salmon"])

# Add title and labels
plt.title("Spam vs Ham Message Distribution")
plt.xlabel("Message Type")
plt.ylabel("Number of Messages")

# Show values on bars
plt.xticks(rotation=0)

# Display the graph
plt.tight_layout()
plt.show()

# Message length analysis

df["message_length"] = df["message"].str.len()

print("\nMessage Length:")
print(df[["label", "message_length"]].head())