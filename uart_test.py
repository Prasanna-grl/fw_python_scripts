import serial
import time

# Open serial port (replace 'COMx' or '/dev/ttySx' with your port)
ser = serial.Serial(port='COM3', baudrate=9600, timeout=1)

try:
    while True:
        test_data = b'Hello UART Loopback'  # Data to send
        ser.write(test_data)                 # Write to UART
        print("Sent:", test_data)

        time.sleep(0.1)                     # Small delay

        received_data = ser.read(len(test_data))  # Read the same amount
        print("Received:", received_data)

        if received_data == test_data:
            print("Loopback test successful")
        else:
            print("Loopback test failed")

        time.sleep(1)  # Wait before next send
except KeyboardInterrupt:
    pass
finally:
    ser.close()
