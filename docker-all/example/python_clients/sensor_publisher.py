import requests
import time
import random

SUBSCRIBER_URL = "http://localhost:8083"
SENSOR_ID = "room-temp-sensor-1"

def simulate_temperature():
    return round(random.uniform(18.0, 26.0), 2)

while True:
    temperature = simulate_temperature()
    payload = {
        "sensor_id": SENSOR_ID,
        "temperature": temperature
    }
    try:
        response = requests.post(SUBSCRIBER_URL, json=payload)
        print(f"[📤 SENT] Temp: {temperature}°C to Subscriber ✅")
    except requests.exceptions.RequestException as e:
        print(f"[🚨] Failed to send data: {e}")
    time.sleep(10)
