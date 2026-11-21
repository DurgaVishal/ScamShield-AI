
import streamlit as st
import joblib
from risk_indicators import detect_risk_indicators

# Load trained model and vectorizer
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
    background-color: #0f172a;
    color: white;
}

h1, h2, h3 {
    color: #60a5fa;
}

.stTextArea textarea {
    background-color: #1e293b;
    color: white;
}

.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# App title
st.title("🛡️ ScamShield AI")
st.caption("AI-powered SMS spam and scam detection")

st.markdown("Enter a message below to analyze it.")

# Message input
message = st.text_area(
    "Enter SMS message",
    height=150,
    placeholder="Paste your suspicious message here..."
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

        # Detect risk indicators
        risk_indicators = detect_risk_indicators(message)

        # Calculate risk score
        risk_score = len(risk_indicators)

        if risk_score <= 1:
            risk_level = "LOW"
        elif risk_score <= 3:
            risk_level = "MEDIUM"
        else:
            risk_level = "HIGH"

        # Get prediction probabilities
        probabilities = model.predict_proba(message_vector)[0]
        confidence = max(probabilities) * 100

        # Analysis results
        st.markdown("---")
        st.subheader("Analysis Result")

        # Spam result
        if prediction == "spam":
            st.error("🚨 SPAM MESSAGE DETECTED!")
        else:
            st.success("✅ This message appears to be NORMAL.")

        # Model confidence
        st.metric("Model Confidence", f"{confidence:.2f}%")

        # Prediction probability
        st.subheader("Prediction Probability")

        normal_probability = probabilities[0] * 100
        spam_probability = probabilities[1] * 100

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Normal Message", f"{normal_probability:.2f}%")

        with col2:
            st.metric("Spam Message", f"{spam_probability:.2f}%")

        # Risk score section
        st.markdown("---")
        st.subheader("🚦 Scam Risk Assessment")

        if risk_level == "LOW":
            st.success(f"🟢 Risk Level: {risk_level}")
        elif risk_level == "MEDIUM":
            st.warning(f"🟡 Risk Level: {risk_level}")
        else:
            st.error(f"🔴 Risk Level: {risk_level}")

        st.metric("Risk Score", f"{risk_score} indicators detected")

        # Risk indicators
        st.subheader("🛡️ Scam Risk Indicators")

        if risk_indicators:
            st.write("Potential warning signs detected:")

            for indicator in risk_indicators:
                st.write(f"⚠️ {indicator}")

        else:
            st.success("No rule-based risk indicators detected.")

        # Disclaimer
        st.caption(
            "Risk indicators are keyword-based signals and do not confirm "
            "that a message is a scam. ML predictions may also be incorrect."
        )
