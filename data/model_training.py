
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load cleaned dataset
df = pd.read_csv("data/processed/sms_cleaned.csv")

# Separate messages and labels
X = df["message"]
y = df["label"]

# Convert text into numerical features
vectorizer = TfidfVectorizer(max_features=3000)
X_tfidf = vectorizer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf,
    y,
    test_size=0.2,
    random_state=42
)

# Create the machine learning model
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

print("Model training completed!")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# Make predictions on test data
y_pred = model.predict(X_test)

# Check model accuracy
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

import joblib
import os

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save trained model
joblib.dump(model, "models/spam_model.pkl")

# Save TF-IDF vectorizer
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\nModel and vectorizer saved successfully!")