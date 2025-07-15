import google.generativeai as genai  # ✅ This line was missing

# Enter your  API key
genai.configure(api_key="AIzaSyBK5yWIQotaB1G7a23yPQrAYQhyeMCZiaQ")


model = genai.GenerativeModel(model_name="models/chat-bison-001")

# Enter sample prompt
response = model.generate_content("Enter a prompt")

# Output the result
print("✅ Gemini says:")
print(response.text)
