from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal.",
    "It always seems impossible until it's done.",
    "Dream big and dare to fail."
]


@app.route("/quote", methods=["GET"])
def get_quote():
    quote = random.choice(quotes)

    return jsonify({
        "quote": quote
    })
@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)