import serial
import time
from recognize import check_face


ser = serial.Serial('/dev/serial0', 115200, timeout=1)

readings = []
window_size = 8
threshold = 15  # you'll want to test and adjust this
cooldown_seconds = 8
last_triggered = 0

def check_camera():
    result = check_face()
    print(f"Camera check result: {result}")

while True:
    line = ser.readline().decode('utf-8', errors='ignore').strip()

    if line.startswith("Range"):
        parts = line.split()
        range_value = int(parts[1])

        readings.append(range_value)

        if len(readings) > window_size:
            readings.pop(1)
        
        spread = max(readings) - min(readings)

        if spread > threshold and time.time() - last_triggered > cooldown_seconds:
            check_camera()
            last_triggered = time.time()
