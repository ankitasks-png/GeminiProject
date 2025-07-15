import requests
import json

# ✅ Replace with your actual Gemini API key
API_KEY = "AIzaSyBK5yWIQotaB1G7a23yPQrAYQhyeMCZiaQ"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json",
}

# 👇 USER INPUT HERE
prompt = input("📝 Enter your prompt: ")

# 💡 Build the request
data = {
    "contents": [
        {
            "parts": [{"text": prompt}]
        }
    ]
}

# 🚀 Send the request
response = requests.post(API_URL, headers=headers, data=json.dumps(data))

# 📦 Handle response
if response.status_code == 200:
    gemini_response = response.json()
    try:
        text_response = gemini_response['candidates'][0]['content']['parts'][0]['text']
        print("\n✅ Gemini says:\n", text_response)
    except (KeyError, IndexError):
        print("⚠️ Unexpected response structure:\n", gemini_response)
else:
    print("❌ Error:", response.status_code, response.text)
