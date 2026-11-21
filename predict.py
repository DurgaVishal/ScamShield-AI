import joblib

# Load the saved model
model = joblib.load("models/spam_model.pkl")

# Load the TF-IDF vectorizer
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Get message from user
message = input("Enter a message to check: ")

# Convert message into numerical features
message_vector = vectorizer.transform([message])

# Predict the message
prediction = model.predict(message_vector)

# Display result
if prediction[0] == "spam":
    print("\n⚠️ SPAM MESSAGE DETECTED!")
else:
    print("\n✅ THIS MESSAGE IS HAM (NORMAL).")