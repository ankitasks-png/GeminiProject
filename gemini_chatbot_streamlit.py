import streamlit as st
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")

st.title("Gemini Chatbot")
prompt = st.text_input("Enter a prompt")

if st.button("Generate"):
    if prompt:
        try:
            response = model.generate_content(prompt)
            st.write("### Gemini says:")
            st.success(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a prompt.")
