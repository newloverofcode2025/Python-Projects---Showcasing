# Battery Notification 🔋

A Python script that monitors your laptop's battery percentage and sends desktop notifications when the battery is low or fully charged.

## Prerequisites
- Python 3.x
- `psutil` and `plyer` packages

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BatteryNotification.git
   cd BatteryNotification
   ```
2. Install the required packages:
   ```bash
   pip install psutil plyer
   ```

## How to Run
1. Run the script:
   ```bash
   python battery_notification.py
   ```

2. (Optional) You can specify the check interval (in seconds) as an argument:
   ```bash
   python battery_notification.py 120
   ```

## Logging
The script logs its activity, including battery status checks and notifications sent, to the console.