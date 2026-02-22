import streamlit as st
import joblib
import re

model = joblib.load("mental_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="Mental Health Analyzer", page_icon="🧠")
st.title("🧠 Mental Health Sentiment Analyzer")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

user_input = st.text_area("Enter text to analyze")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter text.")
    else:
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]
        probabilities = model.predict_proba(vector)[0]

        st.subheader("Prediction:")
        st.write(f"**{prediction}**")

        st.subheader("Confidence Scores:")
        for label, prob in zip(model.classes_, probabilities):
            st.write(f"{label}: {round(prob*100,2)}%")

        if prediction == "Distress":

            st.error("⚠ If you are struggling, consider seeking support from a trusted person or professional.")
