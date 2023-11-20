import serial
import time

with serial.Serial('COM6', 9600, timeout=1) as ser:
    print(f"Serial port {ser.name} opened.")
    data = []
    readings = []
    while True:
        st = time.time()
        ser.reset_input_buffer()

        incoming = ser.readline().decode()

        if incoming:
            readings.append(incoming)
            newtime = time.time()
            # print rows per second
            et = time.time()
            data.append(1 / (et - st + 0.00000001))
            print(f"\raverage Hertz: {sum(data)/len(data)}", end="")
        else:
            print(f"\rNo data received", end="")
            time.sleep(1)
            continue