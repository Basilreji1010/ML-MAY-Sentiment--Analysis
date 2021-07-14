import streamlit as st
import joblib
st.title('Spam Ham Deployment')
st.title('Sentiment Analysis Deployment')
test_model = joblib.load('Sentiment-Analysis')
ip = st.text_input('Enter your message')
op = test_model.predict([ip])
