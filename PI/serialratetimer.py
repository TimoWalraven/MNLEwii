""""For measuring the rate of serial communication between the PI zero series"""

import serial
import numpy as np
import time

title = "PI Zero W"
port = 'COM6'
test_length = 5  # seconds

times = []
intervals = []

if __name__ == "__main__":
    print("Opening serial port...")
    with serial.Serial(port, 9600, timeout=1) as ser:
        print(f"Serial port {ser.name} opened.")
        # countdown 5 seconds
        for i in range(5, 0, -1):
            print(f"Starting in {i}...")
            time.sleep(1)
        print("Starting test...")
        start_time = time.time()
        while True:
            if time.time() - start_time > test_length:
                print(f"Test finished, closing serial port {ser.name}...")
                break
            elif ser.in_waiting:
                newtime = time.time()
                times.append(newtime - start_time)
                try:
                    intervals.append(newtime - (times[-2]+start_time))
                except IndexError:
                    intervals.append(0)

                temp = ser.readline().decode()
                print(temp)

    # convert data to numpy array
    recording = np.array([times, intervals])
    print(recording)

    # plot histogram of intervals
    import matplotlib.pyplot as plt
    plt.hist(intervals)
    plt.title(f"Intervals for {title}")
    plt.show()

    # save data to file
    np.savetxt('serial_data.csv', recording, delimiter=',')
    print("Data saved to file.")
