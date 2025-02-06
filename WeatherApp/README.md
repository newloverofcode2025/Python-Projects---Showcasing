# Weather App

This is a simple weather application built with Flask that fetches weather data from the OpenWeatherMap API.

## Features

- Fetches current weather data for a specified city.
- Displays city name, temperature, and weather description.

## Requirements

- Python 3.x
- Flask
- Requests

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your OpenWeatherMap API key:

    ```sh
    export OPENWEATHERMAP_API_KEY='your_api_key'  # On Windows use `set OPENWEATHERMAP_API_KEY=your_api_key`
    ```

## Usage

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter a city name and click "Get Weather" to see the current weather data.

## Project Structure

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/1) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Requests](https://docs.python-requests.org/)
- [OpenWeatherMap API](https://openweathermap.org/api)