import psutil
from plyer import notification
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_battery_info():
    """Fetches battery information."""
    battery = psutil.sensors_battery()
    if battery is None:
        logging.error("No battery detected.")
        return None
    percent = battery.percent
    plugged = battery.power_plugged
    return percent, plugged

def send_notification(title, message):
    """Sends a desktop notification."""
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification stays for 10 seconds
    )

def monitor_battery(check_interval=60):
    """Monitors battery and sends notifications."""
    try:
        while True:
            battery_info = get_battery_info()
            if battery_info:
                percent, plugged = battery_info
                if percent <= 20 and not plugged:
                    send_notification("Low Battery", f"Battery at {percent}%! Please plug in your charger.")
                    logging.info(f"Low Battery: {percent}%")
                elif percent >= 90 and plugged:
                    send_notification("Battery Full", "Battery is fully charged. You can unplug the charger.")
                    logging.info("Battery Full")
            time.sleep(check_interval)  # Check every `check_interval` seconds
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")

if __name__ == "__main__":
    logging.info("Monitoring battery status...")
    monitor_battery()