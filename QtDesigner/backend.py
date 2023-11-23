import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QTimer
from threading import Thread
import serial
from serial.tools import list_ports
import datetime
from time import sleep

import frontend
import pandas as pd
import numpy as np


class STEPviewer:

    def __init__(self, dummy=False):
        # Setup frontend
        self.app = QApplication.instance()  # checks if QApplication already exists
        if not self.app:  # create QApplication if it doesn't exist
            self.app = QApplication(sys.argv)
        self.ui = frontend.Ui_MainWindow()
        self.win = QMainWindow()
        self.ui.setupUi(self.win)

        # global variables
        self.mode = 'live'
        self.livex = []
        self.livey = []
        self.analysdata = pd.DataFrame(columns=['time', 'x', 'y'])

        if dummy:
            self.dummyrec = pd.read_csv('dummyrec.csv', sep=' ', header=0)
            self.livex = self.dummyrec['x'].tolist()
            self.livey = self.dummyrec['y'].tolist()

        self.display = False

        # Live mode variables
        self.status = 'Disconnected'

        self.com_list = []
        self.com_port_selected = None

        self.recording = []
        self.recordstate = False

        # Analysis mode variables

        # Live mode setup
        # Toolbar
        self.ui.startrecording.clicked.connect(self.recorder)  # record button
        self.ui.saverecording.clicked.connect(self.saverecording)  # save button
        # Plots
        self.ui.liveapwidget.setmode('AP')
        self.ui.livemlwidget.setmode('ML')

        # Initialize timer for updating the plot and elapsed time
        self.start_time = datetime.datetime.now()
        self.interval = 10  # Interval in milliseconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(self.interval)  # Start the timer

        # threading
        self.readthread = Thread(target=self.read_from_serial)
        self.readthread.daemon = True  # Daemon threads are terminated when the main program exits.
        self.readthread.start()

        # start application
        self.win.show()
        print("GUI initialized.")
        self.app.exec()

    def update_com(self):
        '''
        Method that get the lost of available coms in the system
        '''

        # update com list
        ports = list_ports.comports()
        if len(ports) == 0:
            self.com_list = ['No com ports found']
        else:
            self.com_list = [com[0] for com in ports]

        # update com port dropdown
        if self.ui.comport.currentText() not in self.com_list:
            self.ui.comport.clear()
            self.ui.comport.addItems(self.com_list)

    def read_from_serial(self):
        while self.mode == 'live':
            self.display = False
            if self.com_port_selected != self.ui.comport.currentText() and self.ui.comport.currentText() in self.com_list:
                self.com_port_selected = self.ui.comport.currentText()
                print(f'com port selected: {self.com_port_selected}')
            if self.com_port_selected is not None and self.com_port_selected != 'No com ports found':
                try:
                    with serial.Serial(self.com_port_selected, 115200, timeout=1) as ser:
                        print(f"Serial port {ser.name} successfully opened.")
                        self.display = True
                        line = ''
                        while self.com_port_selected == self.ui.comport.currentText():
                            incoming = ser.readline().decode()
                            if incoming and incoming != '':
                                line += incoming[1:-2]
                                self.livex.append(float(line.split(', ')[0]))
                                self.livey.append(float(line.split(', ')[1]))
                                line = ''
                                if len(self.x) > 30:
                                    self.livex.pop(0)
                                    self.livey.pop(0)
                            else:
                                continue

                except serial.SerialException as e:
                    print(f"An error occurred: {e} \n Trying to reconnect...")
                    self.display = False
                    sleep(1)
            else:
                sleep(1)

    def update(self):
        # Get current mode
        if self.ui.modes.currentIndex() == 0:
            self.mode = 'live'
        elif self.ui.modes.currentIndex() == 1:
            self.mode = 'analysis'

        # Live mode
        if self.mode == 'live':
            self.ui.livestabilogramwidget.line.setData(self.livex, self.livey)
            self.ui.liveapwidget.line.setData(np.linspace(0, 30, len(self.livey)), self.livey)
            self.ui.livemlwidget.line.setData(np.linspace(0, 30, len(self.livex)), self.livex)
            # Status light
            if self.display and self.ui.statuslight.styleSheet() != "background-color: green; border-radius: 10px":
                self.ui.statuslight.setStyleSheet("background-color: green; border-radius: 10px")
            elif not self.display and self.ui.statuslight.styleSheet() != "background-color: red; border-radius: 10px":
                self.ui.statuslight.setStyleSheet("background-color: red; border-radius: 10px")
            # com port selection
            self.update_com()
            # Status text
            if self.ui.comport.currentText() != self.status:
                self.ui.comport.setCurrentText(self.status)




        # Analysis mode
        elif self.mode == 'analysis':
            none = None

        QApplication.processEvents()

    def saverecording(self):
        # TODO: add metadata to file
        if not self.recording:
            print("No recording found.")
            return
        elif self.recordstate:
            print("Recording in progress, please wait for recording to finish.")
            return
        filename = QFileDialog.getSaveFileName(self.window, 'Save File', '', 'CSV(*.csv)')
        with open(filename[0], 'w') as f:
            f.write('"time" "x" "y"\n')
            for line in self.recording:
                f.write(f"{line[0]} {line[1]} {line[2]}\n")

    def recorder(self):
        def record(seconds):
            start_time = datetime.datetime.now()
            times = []
            xs = []
            ys = []

            # record for 10 seconds
            print(f"Recording for {seconds} seconds...")
            while (datetime.datetime.now() - start_time).total_seconds() <= seconds:
                self.recordstate = True
                times.append((datetime.datetime.now() - start_time).total_seconds())
                xs.append(self.x[-1])
                ys.append(self.y[-1])
                sleep(0.01)
            self.recordstate = False
            print("Done.")
            data = []
            for i in range(len(xs)):
                data.append([times[i], xs[i], ys[i]])
            # TODO: execute SWARII resampling on recording
            self.recording = data

        if self.recordstate:
            print("Already recording.")
            return
        elif self.status == 'Disconnected':
            print("No balance board connected.")
            return
        elif self.status == 'Connected':
            recordthread = Thread(target=record, args=(self.ui.recordlength.value(),))
            recordthread.daemon = True
            recordthread.start()
        else:
            print("Unknown error occurred.")

    def play(self):
        self.timer.start(self.interval)

    def pause(self):
        self.timer.stop()

    def slider_changed(self):
        self.idx = self.slider.value()
        self.line.setData(self.x[:self.idx], self.y[:self.idx])

        # Update the elapsed time based on the slider value
        elapsed_time = self.time[self.idx] - self.start_time
        self.time_label.setText(f"Elapsed Time: {elapsed_time:.2f} s")


if __name__ == '__main__':
    plot = STEPviewer(dummy=True)
