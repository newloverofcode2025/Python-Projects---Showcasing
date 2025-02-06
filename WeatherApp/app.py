import os
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Use environment variable for API key
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY', 'your_default_api_key')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found or API request failed'}

    return render_template('home.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)