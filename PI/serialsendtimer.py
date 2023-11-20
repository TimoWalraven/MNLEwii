import time
import random
import serial


if __name__ == "__main__":
    data = 0
    while True:
        try:
            print("Opening serial port...")
            with serial.Serial('/dev/ttyGS0', 9600, timeout=1) as ser:
                print(f"Serial port {ser.name} opened.")
                while True:
                    data = data + random.random()
                    ser.reset_output_buffer()
                    ser.write(f"{str(data)}\n".encode())
                    time.sleep(0.005)
        except serial.SerialException as e:
            print(f"An error occurred: {e}, trying to reconnect...")
            time.sleep(1)
