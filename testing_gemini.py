import google.generativeai as genai  

#   API key
genai.configure(api_key="AIzaSyBK5yWIQotaB1G7a23yPQrAYQhyeMCZiaQ")


model = genai.GenerativeModel(model_name="models/chat-bison-001")

#  sample prompt
response = model.generate_content("Enter a prompt")

# Output 
print(response.text)
