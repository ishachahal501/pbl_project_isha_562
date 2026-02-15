import random
import time
import requests

# Simulated RSSI threshold
RSSI_THRESHOLD = -80

# Simulated IFTTT webhook
IFTTT_WEBHOOK_URL = "https://maker.ifttt.com/trigger/accident_detected/with/key/my_ifttt_key"

def simulate_rssi():
    """Simulate RSSI values with occasional drops"""
    return random.choice([-60, -65, -70, -75, -85, -90])

def send_cloud_alert(rssi):
    """Simulate sending a cloud alert"""
    print(f"[ALERT] RSSI dropped to {rssi}. Accident-like event detected.")
    # Uncomment below to send real webhook
    # requests.get(IFTTT_WEBHOOK_URL)

def monitor_signal():
    """Main loop to monitor RSSI and trigger alerts"""
    print("Starting Wi-Fi signal monitoring...\n")
    for _ in range(10):
        rssi = simulate_rssi()
        print(f"Current RSSI: {rssi}")
        if rssi < RSSI_THRESHOLD:
            send_cloud_alert(rssi)
        time.sleep(2)

if __name__ == "__main__":
    monitor_signal()
