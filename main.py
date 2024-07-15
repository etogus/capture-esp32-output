import serial
import time

ser = serial.Serial(
    port='COM7',
    baudrate=115200,
    timeout=1
)

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Serial reading stopped")
finally:
    ser.close()