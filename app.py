
import streamlit as st
import joblib

# Load trained model and TF-IDF vectorizer
model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Page configuration
st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>

.stApp {
    background-color: #0B1120;
    color: #E5E7EB;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    color: #60A5FA !important;
    font-weight: 800;
}

h2, h3 {
    color: #93C5FD !important;
}

.stTextArea textarea {
    background-color: #161F30 !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
}

.stButton button {
    background-color: #2563EB !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 0.6rem 1.2rem !important;
    font-weight: 600 !important;
}

.stButton button:hover {
    background-color: #1D4ED8 !important;
}

</style>
""", unsafe_allow_html=True)

# App header
st.title("🛡️ ScamShield AI")
st.subheader("Intelligent SMS Spam Detection")

st.write(
    "Analyze SMS messages using machine learning "
    "to identify spam and suspicious messages."
)

st.markdown("---")

# Message input
message = st.text_area(
    "📩 Enter your message",
    placeholder="Paste your SMS message here...",
    height=150
)

# Analyze button
if st.button("🔍 Analyze Message", use_container_width=True):

    if message.strip() == "":
        st.warning("Please enter a message first.")

    else:
        # Convert message into numerical features
        message_vector = vectorizer.transform([message])

        # Predict message category
        prediction = model.predict(message_vector)[0]

        # Get prediction probability
        probabilities = model.predict_proba(message_vector)[0]
        confidence = max(probabilities) * 100

        st.markdown("---")
        st.subheader("Analysis Result")

        # Spam result
        if prediction == "spam":

            st.error("🚨 SPAM MESSAGE DETECTED!")

            st.write(
                "This message may be unwanted, fraudulent, "
                "or suspicious. Be careful before responding."
            )

        # Normal message result
        else:

            st.success("✅ NORMAL MESSAGE (HAM)")

            st.write(
                "This message appears to be a normal SMS."
            )
        # Prediction probabilities
        st.markdown("### 📊 Prediction Breakdown")

        normal_probability = probabilities[0] * 100
        spam_probability = probabilities[1] * 100

        st.write(f"🟢 Normal Message: **{normal_probability:.2f}%**")
        st.progress(float(normal_probability / 100))

        st.write(f"🔴 Spam Message: **{spam_probability:.2f}%**")
        st.progress(float(spam_probability / 100))
        st.write(f"Model confidence: **{confidence:.2f}%**")

st.markdown("---")

# Footer
st.caption("🛡️ ScamShield AI | Machine Learning SMS Protection")
