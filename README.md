# Serial Data Logger for Binary Output

This Python script captures and logs data from a serial port.<br>

This script is a part of the larger project "Extraction of the SRAM-based PUF on the ESP32 platform":<br>
https://github.com/etogus/esp32-sram-puf

## Features

- Reads serial data from a specified COM port
- Parses incoming data using regular expressions
- Logs strings to separate files
- Real-time console output of received data

## Requirements

- Python 3.x
- pyserial library

## Usage

1. Ensure your device is connected to the specified COM port (default is COM7)
2. Run the script:
3. The script will create two txt files in the same directory:
- `binary_before.txt`: Contains binary strings logged before initialization
- `binary_after.txt`: Contains binary strings logged after initialization

4. To stop the script, use Ctrl+C

## Configuration

You may need to modify the following parameters in the script:

- `port`: Set this to match your device's COM port
- `baudrate`: Adjust if your device uses a different baud rate

## Note

This script is designed to work with a specific output format. Ensure your device outputs data in the expected format:<br>
`I (timestamp) BEFORE/AFTER: Binary: [binary_string]`

For any other format, you may need to adjust the regular expression pattern in the script.
