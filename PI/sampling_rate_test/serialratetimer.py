""""For measuring the rate of serial communication between the PI zero series"""

from serial import Serial
import numpy as np
import time

### Variables ###
port = 'COM6'
test_length = 5  # seconds

save = True
filename = 'sampling_test_Zero_W_1'

plot = True
#################

times = []

if __name__ == "__main__":
    print("Opening serial port...")
    with Serial(port, 9600, timeout=1) as ser:
        print(f"Serial port {ser.name} opened.")
        # list p

        # countdown 5 seconds
        for i in range(5, 0, -1):
            print(f"Starting in {i}...")
            time.sleep(1)
        print("Starting test...")

        start_time = time.time()
        oldcoming = None

        while True:
            if time.time() - start_time > test_length:
                print(f"Test finished, closing serial port {ser.name}...")
                break
            elif ser.in_waiting and ser.read:
                times.append(time.time())
                incoming = ser.readline().decode()
                if incoming != oldcoming:
                    oldcoming = incoming

    # convert data to numpy array
    recording = np.array(times)
    intervals = np.diff(recording)
    print(f"Number of intervals: {len(intervals)}")
    # print average interval
    print(f"Average interval: {np.mean(intervals)}")
    # plot histogram of intervals

    if plot:
        import matplotlib.pyplot as plt
        plt.hist(intervals, bins=70, range=(0, 0.07))
        plt.xlabel("Interval (s)")
        plt.ylabel("Count")
        plt.title('Signal variance')
        plt.show()
    if save:
        np.savetxt(f"{filename}.csv", intervals, delimiter=';')
        print("Data saved to file.")
