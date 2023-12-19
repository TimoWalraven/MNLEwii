""""For measuring the rate of serial communication between the PI zero series"""

from serial import Serial
import numpy as np
import time
import os.path

### Variables ###
port = 'COM6'
test_length = 20  # seconds

save = True
filename = 'Zero W/20s_nosleep_nowobble'

plot = True
#################

times = []

if __name__ == "__main__":
    print("Opening serial port...")
    with Serial(port, 9600, timeout=1) as ser:
        print(f"Serial port {ser.name} opened.")
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
        if filename == '':
            filename = input("Enter filename: ")
        elif filename[-4:] == '.csv':
            filename = filename[:-4]
        #check if file exists, if so, add number to end
        elif os.path.isfile(f"{filename}.csv"):
            i = 1
            while os.path.isfile(f"{filename}({i}).csv"):
                i += 1
            filename = f"{filename}({i})"
        np.savetxt(f"{filename}.csv", intervals, delimiter=';', fmt='%1.5f')
        print("Data saved to file.")
