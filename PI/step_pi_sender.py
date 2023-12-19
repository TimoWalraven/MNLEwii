import sys
import time
from typing import Optional
import evdev
from evdev import ecodes
from serial import Serial

def get_board_device() -> Optional[evdev.InputDevice]:
    """ Return the Wii Balance Board device. """
    devices = [
        path
        for path in evdev.list_devices()
        if evdev.InputDevice(path).name == "Nintendo Wii Remote Balance Board"
    ]
    if not devices:
        return None

    board = evdev.InputDevice(
        devices[0],
    )
    return board


def get_raw_measurement(device: evdev.InputDevice):
    """Read one measurement from the board."""
    data = [None] * 4
    length = 228
    width = 433
    tries = 50
    while True:
        event = device.read_one()
        if event is None:
            continue
        # Measurements are in decigrams, so we convert them to kilograms here.
        if event.code == ecodes.ABS_HAT1X:
            # Top left.
            data[0] = event.value
        elif event.code == ecodes.ABS_HAT0X:
            # Top right.
            data[1] = event.value
        elif event.code == ecodes.ABS_HAT0Y:
            # Bottom left.
            data[2] = event.value
        elif event.code == ecodes.ABS_HAT1Y:
            # Bottom right.
            data[3] = event.value
        elif event.code == ecodes.BTN_A:
            sys.exit("ERROR: User pressed board button while measuring, aborting.")
        elif event.code == ecodes.SYN_DROPPED:
            pass
        elif event.code == ecodes.SYN_REPORT and event.value == 3:
            pass
        elif event.code == ecodes.SYN_REPORT and event.value == 0:
            # TODO: optimise cpu usage when no event is received
            if None in data:
                if tries == 0:
                    time.sleep(1)
                else:
                    tries -= 1
                # This measurement failed to read one of the sensors, try again.
                data = [None] * 4
                continue
            else:
                # calculate x and y cop coordinates in mm
                x_cop = width/2 * (data[1] + data[2] - data[0] - data[3]) / sum(data)
                y_cop = length/2 * (data[0] + data[1] - data[2] - data[3]) / sum(data)
                return [x_cop, y_cop]
        else:
            print(f"ERROR: Got unexpected event: {evdev.categorize(event)}")


if __name__ == "__main__":
    print("Waiting for board...")
    boardfound = None
    while not boardfound:
        boardfound = get_board_device()
        if boardfound:
            print("Board found!")
            break
        time.sleep(1)
    print("Opening serial port...")
    with Serial('/dev/ttyGS0', 9600, timeout=1) as ser:
        print(f"Serial port {ser.name} opened.")
        while True:
            try:
                data = get_raw_measurement(boardfound)
            except Exception as e:
                print("Exception, closing serial port...")
                break

            data = [round(i, 4) for i in data]
            ser.reset_output_buffer()
            ser.write(f"{str(data)}\n".encode())
            time.sleep(0.01)

    print(f"Serial port {ser.name} closed.")
    print("Exiting...")

