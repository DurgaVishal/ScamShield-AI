import pandas as pd
import re

# Load the cleaned dataset
data_path = "data/processed/sms_cleaned.csv"

df = pd.read_csv(data_path)

# Function to clean text
def clean_text(text):
    text = text.lower()                     # Convert to lowercase
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-z\s]", "", text)   # Remove numbers & symbols
    text = re.sub(r"\s+", " ", text).strip() # Remove extra spaces
    return text

# Apply cleaning to messages
df["clean_message"] = df["message"].apply(clean_text)

# Display results
print(df[["message", "clean_message"]].head())