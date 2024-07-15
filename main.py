import serial
import time
import re

# Serial config
ser = serial.Serial(
    port='COM7',
    baudrate=115200,
    timeout=None
)

# Clear input buffer
ser.reset_input_buffer()

# Pattern to match the desired lines
pattern = r'I \(\d+\) (BEFORE|AFTER): Binary: ([01]+)'

# Files to write to
file_before_init = open('binary_before.txt', 'w')
file_after_init = open('binary_after.txt', 'w')

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            match = re.search(pattern, line)
            if match:
                before_after = match.group(1)
                binary = match.group(2)
                output = f"{binary}\n"
                print(f"Writing: {output.strip()}")
                if before_after == "BEFORE":
                    file_before_init.write(output)
                    file_before_init.flush()
                elif before_after == "AFTER":
                    file_after_init.write(output)
                    file_after_init.flush()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Serial reading stopped")
finally:
    ser.close()
    file_before_init.close()
    file_after_init.close()