from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyCIrzuEQRtPgz49IPsX2UtWdbr_QEB5pGU"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": API_KEY
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_input
                    }
                ]
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    try:
        reply = data['candidates'][0]['content']['parts'][0]['text']
    except:
        reply = "Sorry, AI couldn't respond."
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
