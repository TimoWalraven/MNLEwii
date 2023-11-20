import sys
from datetime import datetime
import time
from typing import Optional

import evdev
from evdev import ecodes


def get_board_device() -> Optional[evdev.InputDevice]:
    """Return the Wii Balance Board device."""
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
            if None in data:
                # This measurement failed to read one of the sensors, try again.
                data = [None] * 4
                continue
            else:
                # calculate x and y cop coordinates
                x_cop = (data[1] + data[2] - data[0] - data[3]) / sum(data)
                y_cop = (data[0] + data[1] - data[2] - data[3]) / sum(data)
                return [x_cop, y_cop]  # type: ignore
        else:
            print(f"ERROR: Got unexpected event: {evdev.categorize(event)}")


if __name__ == "__main__":
    boardfound = None
    while not boardfound:
        boardfound = get_board_device()
        if boardfound:
            print("\aBalance board found, please step on.")
            break
        time.sleep(0.5)
    count = 0
    starttime = time.time()
    while True:
        # get bluetooth data refresh rate
        try:
            data = boardfound.read_one()
            count += 1
        except BlockingIOError:
            continue
        except OSError:
            continue
        timedelta = time.time() - starttime
        print(f"\rBluetooth data refresh rate: {count/timedelta}", end="")
