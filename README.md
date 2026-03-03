#  Mental Health Sentiment Analyzer

A Machine Learning web application that analyzes user-entered text and predicts mental health sentiment in real time.

This project demonstrates the complete ML pipeline — from text preprocessing and model training to deployment using Streamlit Cloud.

---

##  Live Demo

🌐 https://mental-health-sentiment-analyzer-bjfxszj64w8yqqz882d8qc.streamlit.app/

---

##  Project Overview

The Mental Health Sentiment Analyzer allows users to:

- Enter any text input
- Analyze sentiment using a trained ML model
- Receive instant prediction results

The application is designed as a beginner-friendly NLP deployment project.

---

##  Tech Stack

- Python
- Scikit-learn
- Natural Language Processing (TF-IDF Vectorization)
- Streamlit
- Joblib

---

##  How It Works

1. Text input is collected from the user.
2. Text is transformed using a trained TF-IDF vectorizer.
3. The saved ML model predicts the sentiment.
4. The result is displayed instantly in the web interface.

---

## 📂 Project Structure

```
mental-health-sentiment-analyzer/
│
├── app.py
├── mental_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## ⚙ Installation (Run Locally)

Clone the repository:

```bash
git clone https://github.com/aslimfathima15/mental-health-sentiment-analyzer.git
cd mental-health-sentiment-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 🎯 Learning Outcomes

- Understanding text preprocessing
- Feature extraction using TF-IDF
- Model training and serialization
- Deploying ML applications using Streamlit Cloud
- Managing dependencies with requirements.txt

---

## 📌 Future Improvements

- Add model confidence scores visualization
- Improve dataset size and accuracy
- Deploy using Docker
- Add user authentication

---

## 👩‍💻 Author

Aslim J 
Aspiring ML & Full-Stack Developer  

---
