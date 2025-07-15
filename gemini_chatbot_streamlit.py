import streamlit as st
import google.generativeai as genai

#  API key
genai.configure(api_key="AIzaSyBK5yWIQotaB1G7a23yPQrAYQhyeMCZiaQ")


model = genai.GenerativeModel(model_name="models/chat-bison-001")

st.set_page_config(page_title="Gemini Chatbot", layout="centered")

st.title("💬 Ankita's Gemini AI Chatbot")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if prompt.strip():
        try:
            response = model.generate_content(prompt)
            st.markdown(" Gemini says:")
            st.success(response.text)
        except Exception as e:
            st.error(f" Error: {e}")
    else:
        st.warning("Please type something before clicking Generate!")
