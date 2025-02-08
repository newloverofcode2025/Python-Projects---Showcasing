# 🌦️ Automated Weather Report Script with Python

## 👋 Welcome!

This repository contains a Python script that fetches the current weather information for a specified city from the [OpenWeatherMap API](https://openweathermap.org/) and displays a formatted weather report in the console.

**Purpose:**

*   Demonstrates how to interact with web APIs using Python.
*   Shows how to parse JSON data from API responses.
*   Provides a simple command-line tool to get weather information quickly.
*   Good example for learning about API keys and environment variables for security.

**Features:**

*   **Fetches current weather data:**  Retrieves weather information from OpenWeatherMap API for a given city.
*   **Formatted Report:**  Displays weather description, temperature (Celsius), humidity, and wind speed in a readable format.
*   **Error Handling:** Handles API request errors and cases where weather data is not found.
*   **Secure API Key Handling:**  Retrieves API key from an environment variable for security (API key is not hardcoded in the script).

**Files in this Repository:**

*   **`weather_report.py`:** The Python script to fetch and display weather reports.
*   **`README.md`:** This file, providing information about the project.

## 🚀 Getting Started

**Prerequisites:**

*   **Python 3.x:**  Make sure you have Python 3 installed.
*   **`requests` library:**  Used to make HTTP requests to the OpenWeatherMap API.
*   **OpenWeatherMap API Key:** You need to sign up for a free account at [https://openweathermap.org/](https://openweathermap.org/) and obtain an API key (see Step 4 in the project instructions).

**Installation and Setup:**

1.  **Clone this repository (if using Git):**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
    cd AutomatedWeatherReport # Or the folder name you used
    ```
    Or **download the ZIP file** and extract it.

2.  **(Recommended) Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Activate virtual environment (Windows)
    ```

3.  **Install `requests` library:**
    ```bash
    pip install requests
    ```
    **(Ensure your virtual environment is activated when running `pip install`).**

4.  **Set the `OPENWEATHERMAP_API_KEY` environment variable:**

    *   **For testing (current terminal session only):** In your activated terminal, run:
        ```bash
        set OPENWEATHERMAP_API_KEY=YOUR_API_KEY_HERE  # Replace with your actual API key
        ```
    *   **For permanent environment variable (recommended for regular use):**  See instructions in Step 6 of the project guide in the main prompt for setting environment variables permanently in Windows system settings.  (Remember to restart VS Code or your computer after setting permanent environment variables for them to be recognized).

**Running the Script:**

1.  **Open a terminal or command prompt.**
2.  **Navigate to the project directory:**
    ```bash
    cd path\to\your\AutomatedWeatherReport # Replace with your actual path
    ```
3.  **(Activate virtual environment if you created one):**
    ```bash
    .venv\Scripts\activate
    ```
4.  **Make sure you have set the `OPENWEATHERMAP_API_KEY` environment variable (as described above).**
5.  **Run the script:**
    ```bash
    python weather_report.py
    ```
6.  **Enter city name when prompted:** The script will ask you to enter a city name. Type the city name and press Enter.
7.  **View the Weather Report:** The script will display the formatted weather report for the city in the console.

**Customization and Enhancements (Ideas for improvement):**

*   **More Weather Details:**  Expand the report to include more weather parameters from the API response (e.g., feels like temperature, pressure, sunrise/sunset times, detailed weather conditions, etc.). Refer to the OpenWeatherMap API documentation for available data.
*   **Forecast Data:**  Modify the script to fetch and display weather forecasts (e.g., daily forecast for the next few days). OpenWeatherMap has forecast APIs as well.
*   **Error Handling Improvements:**  Add more robust error handling, such as checking for invalid city names or API key errors, and providing more informative error messages to the user.
*   **Units Configuration:** Allow users to choose units (e.g., Celsius or Fahrenheit, metric or imperial) through command-line arguments or configuration files.
*   **Graphical Output/GUI:** Instead of console output, create a simple GUI application to display the weather report visually using libraries like Tkinter or PyQt.
*   **Save Reports to File:**  Add an option to save weather reports to a text file or other formats.
*   **Recurring Weather Updates (Scheduling):** Use Windows Task Scheduler or similar tools to schedule the script to run automatically at regular intervals and save weather reports, or send notifications.

## 📜 License

This project is licensed under the [MIT License](LICENSE).


**Enjoy getting your automated weather reports! 🌦️**