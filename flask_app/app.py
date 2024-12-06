from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    user_message = request.json.get("message")
    payload = {"sender": "user", "message": user_message}
    response = requests.post(RASA_URL, json=payload)
    bot_messages = response.json()
    return jsonify(bot_messages)

if __name__ == "__main__":
    app.run(port=5000)
