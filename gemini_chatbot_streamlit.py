import streamlit as st
import google.generativeai as genai

# 🔐 API Key via Streamlit secrets
genai.configure(api_key=st.secrets["api_key"])

# ✅ Use older supported model for Streamlit Cloud
model = genai.GenerativeModel(model_name="models/chat-bison-001")

# 🎨 Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")
st.title("💬 Gemini Chatbot (Gen AI Bootcamp Project)")
st.markdown("Ask something to Gemini:")

# 📝 User input
prompt = st.text_input("")

if st.button("Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        try:
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                st.success("Here's what Gemini says:")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")
