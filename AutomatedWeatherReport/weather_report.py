import requests
import json
import os  # For environment variables

def get_weather_data(city_name, api_key):
    """
    Fetches current weather data from OpenWeatherMap API for a given city.

    Args:
        city_name (str): The name of the city.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        dict: Weather data in JSON format if successful, None otherwise.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"  # API endpoint
    params = {
        'q': city_name,      # City name
        'appid': api_key,    # Your API key
        'units': 'metric'    # Use Celsius for temperature, meters per second for wind
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json() # Parse JSON response
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

def format_weather_report(weather_data, city_name):
    """
    Formats the weather data into a user-friendly report string.

    Args:
        weather_data (dict): Weather data from OpenWeatherMap API.
        city_name (str): The name of the city.

    Returns:
        str: Formatted weather report.
    """
    if not weather_data:
        return "Could not retrieve weather data."

    try:
        city = weather_data['name']
        country = weather_data['sys']['country']
        description = weather_data['weather'][0]['description'].capitalize() # Capitalize description
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        report = (f"--- Weather Report for {city}, {country} ---\n"
                  f"Description: {description}\n"
                  f"Temperature: {temperature}°C\n"
                  f"Humidity: {humidity}%\n"
                  f"Wind Speed: {wind_speed} m/s\n"
                  f"----------------------------")
        return report
    except KeyError: # Handle potential missing data in API response
        return "Error: Incomplete weather data received from API."

def main():
    """Main function to get city name, API key, fetch weather, and print report."""
    city_name = input("Enter city name: ")

    # --- Get API key securely from environment variable ---
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY") # Get API key from environment variable
    if not api_key:
        print("Error: OPENWEATHERMAP_API_KEY environment variable not set.")
        print("Please set your OpenWeatherMap API key as an environment variable.")
        print("Refer to the README for instructions.")
        return

    weather_data = get_weather_data(city_name, api_key)
    if weather_data:
        report = format_weather_report(weather_data, city_name)
        print(report)
    else:
        print(f"Failed to get weather data for {city_name}. Please check city name and API key.")


if __name__ == "__main__":
    main()