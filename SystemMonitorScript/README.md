# 🖥️ System Monitor Script with Python

## 👋 Welcome!

This repository contains a simple Python script to monitor your system's resources (CPU, Memory, Disk) and log the data to a file. It also includes basic alerting for high CPU usage.

**Purpose:**

This script is designed to run in the background and periodically collect system metrics. It can be useful for:

*   **Monitoring system performance:** Track CPU usage, memory consumption, and disk space over time.
*   **Basic alerting:** Get notified if CPU usage exceeds a defined threshold.
*   **Learning system monitoring concepts:** A practical example for understanding how to collect system information with Python.

**Features:**

*   **Monitors:** CPU usage (percentage), Memory usage (percentage), and Free disk space (GB).
*   **Logging:** Records metrics with timestamps to `system_monitor_log.txt`.
*   **CPU Usage Alert:** Prints a warning to the console if CPU usage goes above a threshold (default: 80%).
*   **Configurable:**
    *   **`LOG_FILE`:**  Filename for the log file (default: `system_monitor_log.txt`).
    *   **`CPU_THRESHOLD_PERCENT`:** Percentage of CPU usage to trigger an alert (default: 80%).
    *   **`time.sleep(60)`:**  Monitoring interval (currently set to 60 seconds/1 minute).

**Files in this Repository:**

*   **`system_monitor.py`:** The main Python script for system monitoring and logging.
*   **`system_monitor_log.txt`:** (Will be created when you run the script) The log file where system metrics are recorded.
*   **`README.md`:** This file, providing information about the project.

## 🚀 Getting Started

**Prerequisites:**

*   **Python 3.x:**  Make sure you have Python 3 installed on your Windows system.
*   **`psutil` library:** This script uses the `psutil` library to get system information. You need to install it.

**Installation and Setup:**

1.  **Clone this repository (if you are using Git):**
    ```bash
    ```
    Or **download the ZIP file** of the repository and extract it to your desired location.

2.  **(Recommended) Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Activate the virtual environment (Windows)
    ```

3.  **Install `psutil` library:**
    ```bash
    pip install psutil
    ```
    **(Make sure your virtual environment is activated when running `pip install` - you should see `(.venv)` at the start of your terminal prompt).**

**Running the Script:**

1.  **Open a terminal or command prompt.**
2.  **Navigate to the project directory:**
    ```bash
    cd path\to\your\SystemMonitorScript  # Replace with your actual path
    ```
3.  **(Activate virtual environment if you created one):**
    ```bash
    .venv\Scripts\activate
    ```
4.  **Run the script:**
    ```bash
    python system_monitor.py
    ```

    *   The script will start running and logging system metrics every minute to `system_monitor_log.txt`.
    *   You will see messages in the terminal indicating when metrics are logged.
    *   If CPU usage goes above the threshold, you will see warning messages in the terminal.
    *   To stop the script, press **Ctrl+C** in the terminal.

5.  **Examine the Log File:** Open `system_monitor_log.txt` in a text editor to see the recorded system metrics.

**(Optional) Scheduling the script to run automatically on Windows:**

You can use **Windows Task Scheduler** to run `system_monitor.py` automatically in the background at regular intervals.  See the detailed steps in the previous project instructions for how to set up a scheduled task using Task Scheduler, pointing it to your `system_monitor.py` script and the Python interpreter in your virtual environment.

**Customization:**

*   **`LOG_FILE`:**  Change the `LOG_FILE` variable in `system_monitor.py` to modify the name or path of the log file.
*   **`CPU_THRESHOLD_PERCENT`:**  Adjust `CPU_THRESHOLD_PERCENT` to change the CPU usage threshold for alerts.
*   **`time.sleep(60)`:** Modify the `time.sleep()` value (in seconds) to change the monitoring interval.  For example, `time.sleep(300)` would monitor every 5 minutes. **Be cautious about setting this too low (e.g., less than 10 seconds) as very frequent monitoring might itself consume resources.**

**Possible Enhancements (Ideas for further development):**

*   **Email or other notification alerts:** Instead of just printing to the console, send email or other types of alerts (e.g., push notifications) when thresholds are exceeded.
*   **More metrics:** Monitor other system resources like network usage, specific process CPU/memory usage, GPU usage (if applicable), temperatures, etc.
*   **Configurable thresholds:** Allow users to easily configure thresholds for different metrics.
*   **Data Visualization:**  Create a web interface or use libraries to visualize the logged data over time (e.g., using graphs).
*   **Log rotation:** Implement log rotation to prevent the log file from growing indefinitely.
*   **Cross-platform compatibility:**  Make the script more cross-platform compatible (currently focused on Windows paths).

## 🤝 Contributing

Contributions to improve this script are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.

## 📜 License

This project is licensed under the [MIT License](LICENSE).



**Happy System Monitoring! 🚀**