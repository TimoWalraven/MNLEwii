import time
import serial

data = []

with serial.Serial('COM6', 9600, timeout=1) as ser:
    line = ''
    while True:
        incoming = ser.read()
        if incoming:
            if incoming not in [b'[', b']']:
                line += incoming.decode('utf-8')
            if incoming == b']':
                print(line)
                data.append(line)
                line = ''
            else:
                continue

        else:
            time.sleep(1)
            print("waiting...")
