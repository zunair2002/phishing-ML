import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import requests

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("API KEY:", GROQ_API_KEY)
app = Flask(__name__)
CORS(app)

URL = "https://api.groq.com/openai/v1/chat/completions"

def explain_with_ai(message, label):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "user", 
                "content": f"Explain in 1 simple line why this message is classified as '{label}': {message}"
            }
        ]
    }
    try:
        response = requests.post(URL, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"API Error: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

model = pickle.load(open('model.pkl','rb'))
vectorized = pickle.load(open('vectorized.pkl','rb'))

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json
    text = data['message']
    vector = vectorized.transform([text])
    result = model.predict(vector)[0]

    if result == 1:
        label = "spam"
    else:
        label = "ham"
    explanation = explain_with_ai(text, label)

    return jsonify({
        "result": label,
        "explanation": explanation
    })

if __name__ == '__main__':
    app.run(debug=True)