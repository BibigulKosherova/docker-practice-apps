from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Be yourself; everyone else is already taken.",
    "The only way to do great work is to love what you do.",
    "Life is what happens when you are busy making other plans.",
]

@app.route('/quotes')
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

