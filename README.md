# 🛡️ ScamShield AI

A machine learning-based SMS spam detection application that analyzes text messages and classifies them as **Spam** or **Normal (Ham)**.

## 📌 About the Project

ScamShield AI uses Natural Language Processing (NLP) and machine learning techniques to identify unwanted or potentially fraudulent SMS messages.

Users can enter a message through a simple web interface and receive a prediction along with probability scores for both categories.

## 🎯 Objectives

- Detect spam SMS messages using machine learning.
- Process and clean raw text data.
- Convert text into numerical features using TF-IDF.
- Train and evaluate a classification model.
- Build an interactive web application for real-time predictions.

## ⚙️ Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Streamlit
- Joblib

## 🔄 Machine Learning Workflow

1. Dataset collection
2. Data exploration and analysis
3. Text preprocessing and cleaning
4. Duplicate removal
5. Feature extraction using TF-IDF
6. Model training using Multinomial Naive Bayes
7. Model evaluation
8. Prediction using the trained model
9. Web application development using Streamlit

## 📊 Model Performance

- **Model:** Multinomial Naive Bayes
- **Feature extraction:** TF-IDF
- **Dataset:** SMS Spam Collection
- **Train-test split:** 80:20
- **Accuracy:** Approximately 98%

## 🚀 Features

- SMS message input
- Spam and normal message classification
- Prediction probability breakdown
- Confidence score
- Interactive web interface
- Dark-themed UI

## 💻 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ScamShield-AI.git
```

### 2. Navigate to the project folder

```bash
cd ScamShield-AI
```

### 3. Install dependencies

```bash
pip install pandas scikit-learn streamlit joblib
```

### 4. Run the application

```bash
streamlit run app.py
```

## ⚠️ Disclaimer

ScamShield AI is an educational machine learning project. Its predictions are not guaranteed to identify every spam or fraudulent message. Always verify suspicious messages independently and avoid sharing sensitive information.

## 👩‍💻 Author

Developed as a personal machine learning project to explore NLP, text classification, and deployment of ML models using Streamlit.
