from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

jokes = [
    "What did the ocean say to the beach? Nothing, it just waved.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
    "I threw a boomerang a few years ago. I now live in constant fear."
]

@app.route('/joke')
def get_joke():
    return jsonify({"joke": random.choice(jokes)})

@app.route('/')
def home():
    joke = random.choice(jokes)
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Random Joke</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .joke-box {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                font-size: 1.5rem;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="joke-box">{joke}</div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
