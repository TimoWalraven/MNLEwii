""""For measuring the rate of serial communication between the PI zero series"""

import serial
import numpy as np
import time

title = "PI Zero W"
port = 'COM6'
test_length = 30  # seconds

times = []
data = []
intervals = []

if __name__ == "__main__":
    print("Opening serial port...")
    with serial.Serial(port, 9600, timeout=1) as ser:
        print(f"Serial port {ser.name} opened.")
        start_time = time.time()
        # countdown 5 seconds
        for i in range(5, 0, -1):
            print(f"Starting in {i}...")
            time.sleep(1)
        while True:
            if time.time() - start_time > test_length:
                print(f"Test finished, closing serial port {ser.name}...")
                ser.close()
                print("Serial port closed.")
                break
            elif ser.in_waiting:
                newtime = time.time()
                times.append(newtime - start_time)
                intervals.append(newtime - (times[-1]+start_time))
                data.append(ser.readline())

    # convert data to numpy array
    recording = np.array([times, data, intervals])
    print(recording)

    # plot histogram of intervals
    import matplotlib.pyplot as plt
    plt.hist(intervals)
    plt.show()

    # save data to file
    np.savetxt('serial_data.csv', recording, delimiter=',')
    print("Data saved to file.")
