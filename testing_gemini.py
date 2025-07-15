import google.generativeai as genai  # ✅ This line was missing

# Use your real API key
genai.configure(api_key="AIzaSyBK5yWIQotaB1G7a23yPQrAYQhyeMCZiaQ")

# Use the working model (chat-bison-001)
model = genai.GenerativeModel(model_name="models/chat-bison-001")

# Try a sample prompt
response = model.generate_content("Explain gravity in simple words.")

# Output the result
print("✅ Gemini says:")
print(response.text)
