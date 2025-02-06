from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt"
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)  # Change to debug=False in production