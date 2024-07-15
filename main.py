import serial
import time
import re

ser = serial.Serial(
    port='COM7',
    baudrate=115200,
    timeout=5
)

# Clear input buffer
ser.reset_input_buffer()

# Pattern to match the desired lines
pattern_before = r'I \(\d+\) (BEFORE): Binary: ([01]+)'
pattern_after = r'I \(\d+\) (AFTER): Binary: ([01]+)'
file_before_init = open('binary_before.txt', 'w')
file_after_init = open('binary_after.txt', 'w')

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            match_before = re.search(pattern_before, line)
            if match_before:
                binary = match_before.group(2)
                output = f"{binary}\n"
                print(f"Writing: {output.strip()}")
                file_before_init.write(output)
                file_before_init.flush()
            else:
                match_after = re.search(pattern_after, line)
                if match_after:
                    binary = match_after.group(2)
                    output = f"{binary}\n"
                    print(f"Writing: {output.strip()}")
                    file_after_init.write(output)
                    file_after_init.flush()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Serial reading stopped")
finally:
    ser.close()
    file_before_init.close()
    file_after_init.close()