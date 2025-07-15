import streamlit as st
import google.generativeai as genai

# Set your API key here
genai.configure(api_key="YOUR_API_KEY_HERE")  # <-- Replace with your real API key

# Set up the model
model = genai.GenerativeModel(model_name="models/gemini-pro")

# Streamlit app
st.title("Gemini Chatbot Demo")

prompt = st.text_input("Enter your prompt here:")

if st.button("Generate Response"):
    if prompt:
        try:
            response = model.generate_content(prompt)
            st.subheader("Gemini says:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt before generating.")


