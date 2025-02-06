from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    images = [
        'image1.jpg',
        'image2.jpg',
        'image3.jpg'
    ]
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)