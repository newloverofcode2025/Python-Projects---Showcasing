# src/flask_app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)