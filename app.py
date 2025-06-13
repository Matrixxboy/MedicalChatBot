from flask import Flask, render_template, request, jsonify
from model import chat_replay  # your chat logic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Must match the filename

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    if not user_msg:
        return jsonify({"reply": "Please enter a message."})
    reply = chat_replay(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
