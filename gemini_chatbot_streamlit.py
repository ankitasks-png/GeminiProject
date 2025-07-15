import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit Cloud secrets
genai.configure(api_key=st.secrets["api_key"])

model = genai.GenerativeModel("gemini-pro")

st.title("💬 Gemini Chatbot (Gen AI Bootcamp Project)")
prompt = st.text_input("Ask something to Gemini:")

if st.button("Generate"):
    if prompt:
        try:
            response = model.generate_content(prompt)
            st.success(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a prompt!")
