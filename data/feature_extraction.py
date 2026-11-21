import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("data/processed/sms_cleaned.csv")

# Check available columns
print("Columns:", df.columns.tolist())

# Select message text
if "clean_message" in df.columns:
    X = df["clean_message"]
elif "message" in df.columns:
    X = df["message"]
else:
    print("Message column not found!")
    exit()

# Select labels
y = df["label"]

# Convert text into numerical features
vectorizer = TfidfVectorizer(max_features=3000)

X_tfidf = vectorizer.fit_transform(X)

# Display results
print("\nTF-IDF conversion completed!")
print("Feature matrix shape:", X_tfidf.shape)
print("Number of features:", len(vectorizer.get_feature_names_out()))

print("\nFirst 20 features:")
print(vectorizer.get_feature_names_out()[:20])