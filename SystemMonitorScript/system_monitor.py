import psutil
import datetime
import time

LOG_FILE = "system_monitor_log.txt"
CPU_THRESHOLD_PERCENT = 80  # Alert if CPU usage exceeds 80%

def get_system_metrics():
    """Retrieves system metrics (CPU, memory, disk)."""
    cpu_percent = psutil.cpu_percent(interval=1) # Get CPU usage over 1 second
    memory_usage = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/') # Root partition, adjust if needed

    return {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": cpu_percent,
        "memory_percent": memory_usage.percent,
        "disk_free_gb": disk_usage.free / (1024**3) # Convert free bytes to GB
    }

def log_metrics(metrics, log_filename=LOG_FILE):
    """Appends system metrics to a log file."""
    with open(log_filename, 'a') as logfile: # 'a' for append mode
        log_entry = (f"{metrics['timestamp']}, CPU: {metrics['cpu_percent']:.2f}%, "
                     f"Memory: {metrics['memory_percent']:.2f}%, Disk Free: {metrics['disk_free_gb']:.2f} GB\n")
        logfile.write(log_entry)
    print(f"Logged metrics at {metrics['timestamp']}")

def check_alerts(metrics):
    """Checks for alerts based on system metrics and prints warnings."""
    if metrics['cpu_percent'] > CPU_THRESHOLD_PERCENT:
        print(f"WARNING: High CPU Usage! ({metrics['cpu_percent']:.2f}%) at {metrics['timestamp']}")

def main():
    """Main function to collect, log, and check system metrics."""
    metrics = get_system_metrics()
    log_metrics(metrics)
    check_alerts(metrics)

if __name__ == "__main__":
    while True: # Run continuously in a loop
        main()
        time.sleep(60) # Wait for 60 seconds (1 minute) before next check