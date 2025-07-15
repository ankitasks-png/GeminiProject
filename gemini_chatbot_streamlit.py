import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["AIzaSyBK5yWIQotaB1G7a23yPQrAYQhyeMCZiaQ"])  # Use your actual key locally

model = genai.GenerativeModel(model_name="models/gemini-pro")

st.title("Ankita Gemini Chatbot")

prompt = st.text_input("Ask something:")

if st.button("Generate"):
    if prompt:
        try:
            response = model.generate_content(prompt)
            st.write("Gemini says:")
            st.success(response.text)
        except Exception as e:
            st.error(f" Error: {e}")
    else:
        st.warning("Please enter a prompt.")
