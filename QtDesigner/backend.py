import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QTimer
from threading import Thread
import serial
from serial.tools import list_ports
import datetime
from time import sleep
import numpy as np
# Custom imports
import frontend
from code_descriptors_postural_control.stabilogram.stato import Stabilogram
from code_descriptors_postural_control.descriptors import compute_all_features


class STEPviewer:

    def __init__(self, dummy=False):
        # Setup frontend
        self.app = QApplication.instance()  # checks if QApplication already exists
        if not self.app:  # create QApplication if it doesn't exist
            self.app = QApplication(sys.argv)
        self.ui = frontend.Ui_MainWindow()
        self.win = QMainWindow()
        self.ui.setupUi(self.win)
        self.win.showMaximized()

        # global variables
        self.ui.modes.currentChanged.connect(self.switchmode)
        self.mode = self.ui.modes.currentIndex()

        self.livex = []
        self.livey = []
        self.analysisdata = np.array([])
        self.patientinfo = {
            "stance": "",
            "eyes": "",
            "surface": "",
            "age": "",
            "height": "",
            "weight": "",
            "condition": "",
            "medication": "",
            "notes": ""
        }
        self.idx = 0

        self.display = False

        # Live mode variables
        self.status = 'disconnected'
        self.ui.statustext.setText(f"initializing...")

        self.com_list = []
        self.com_port_selected = None

        self.recording = []
        self.recordstate = False

        if dummy:
            self.dummyrec = np.genfromtxt('dummyrec.csv', delimiter=' ')[1:]
            self.livex = [i[1] for i in self.dummyrec]
            self.livey = [i[2] for i in self.dummyrec]
            self.recording = self.dummyrec

        # Analysis mode variables
        self.analysisidx = 0  # index of current measurement
        self.playstate = False  # state of the play button

        # Live mode setup
        # Toolbar: from left to right
        self.ui.startrecording.clicked.connect(self.recorder)

        self.ui.analyserecording.clicked.connect(self.analyserecording)
        if not dummy:
            self.ui.analyserecording.setDisabled(True)

        # Plots
        self.ui.liveapwidget.setmode('AP')
        self.ui.livemlwidget.setmode('ML')

        # Analysis mode setup
        # Toolbar: from left to right
        # Open file button
        self.ui.analysisopenfile.clicked.connect(self.openrecording)
        # Play/pause button
        self.ui.analysisplay.clicked.connect(self.playpause)
        self.ui.analysisplay.setDisabled(True)
        # Slider current value
        self.ui.currenttime.setText(f'--')
        # Slider
        self.ui.timeslider.valueChanged.connect(self.slider_changed)
        self.ui.timeslider.sliderPressed.connect(self.slider_pressed)
        self.ui.timeslider.sliderReleased.connect(self.slider_released)
        self.ui.timeslider.setDisabled(True)
        self.ui.timeslider.setTracking(True)
        # Slider max value
        self.ui.maxtime.setText(f'--')
        # Restart button
        self.ui.analysisrestart.clicked.connect(self.restart)
        self.ui.analysisrestart.setDisabled(True)
        # Save button
        self.ui.saverecording.clicked.connect(self.saverecording)  # save button
        self.ui.saverecording.setDisabled(True)
        # Widgets
        self.ui.analysisapwidget.setmode('AP')
        self.ui.analysismlwidget.setmode('ML')

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
        while self.mode == 0:
            self.display = False
            if self.com_port_selected != self.ui.comport.currentText() and self.ui.comport.currentText() in self.com_list:
                self.com_port_selected = self.ui.comport.currentText()
                print(f'com port selected: {self.com_port_selected}')
            if self.com_port_selected is not None and self.com_port_selected != 'No com ports found':
                try:
                    print(f"Opening serial port {self.com_port_selected}...")
                    with serial.Serial(self.com_port_selected, 9600, timeout=1) as ser:
                        print(f"Serial port {ser.name} successfully opened.")
                        self.ui.statustext.setText(f"connected")
                        self.display = True
                        line = ''
                        while self.com_port_selected == self.ui.comport.currentText():
                            incoming = ser.readline().decode()
                            if incoming and incoming != '':
                                line += incoming[1:-2]
                                self.livex.append(float(line.split(', ')[0]))
                                self.livey.append(float(line.split(', ')[1]))
                                line = ''
                                if len(self.livex) > 100:
                                    self.livex.pop(0)
                                    self.livey.pop(0)
                            else:
                                continue

                except serial.SerialException as e:
                    print(f"An error occurred: {e} \n Trying to reconnect...")
                    self.status = 'disconnected'
                    self.display = False
                    sleep(1)
            else:
                sleep(1)

    def update(self):
        # TODO: if initialized in mode 1, doesnt connect
        # Live mode
        if self.mode == 0:
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
        elif self.mode == 1:
            if len(self.analysisdata) > 1:
                self.ui.currenttime.setText(f'{self.analysisdata[self.analysisidx][0]:.2f} s')
                time = self.analysisdata[:self.analysisidx, 0]
                x = self.analysisdata[:self.analysisidx, 1]
                y = self.analysisdata[:self.analysisidx, 2]
                self.ui.widget.line.setData(x, y)
                self.ui.analysisapwidget.line.setData(time, y)
                self.ui.analysismlwidget.line.setData(time, x)
                # update plot
                if self.playstate:
                    self.ui.timeslider.valueChanged.disconnect(self.slider_changed)
                    self.ui.timeslider.setValue(self.analysisidx)
                    self.ui.timeslider.valueChanged.connect(self.slider_changed)

                if self.playstate and self.analysisidx < len(self.analysisdata) - 1:
                    self.analysisidx += 1

                elif self.playstate and self.analysisidx >= len(self.analysisdata) - 1:
                    self.playstate = False
                    self.ui.analysisplay.setDisabled(True)
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

    def openrecording(self):
        # ToDo: add option to resample when loading file
        # open file with Qt
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self.win, 'Open CSV File', '', 'CSV Files (*.csv);;All Files (*)',
                                                  options=options)
        try:
            self.analysisdata = np.genfromtxt(fileName, delimiter=' ')[1:]
            self.analysisidx = 0
            self.update()
            self.ui.analysisplay.setDisabled(False)
            self.ui.saverecording.setDisabled(False)
            self.ui.analysisrestart.setDisabled(False)
            self.ui.timeslider.setDisabled(False)
            self.ui.currenttime.setText(f'{self.analysisdata[self.analysisidx][0]:.2f} s')
            self.ui.timeslider.setMaximum(len(self.analysisdata))
            self.ui.maxtime.setText(f'{self.analysisdata[-1][0]:.2f} s')

            # set range of plot by time
            self.ui.analysisapwidget.graph.setRange(xRange=[0, self.analysisdata[-1][0]], yRange=[-115, 115], update=True)
            self.ui.analysismlwidget.graph.setRange(xRange=[0, self.analysisdata[-1][0]], yRange=[-220, 220], update=True)

            print("file read successfully")

        except Exception as e:
            print(f"Error opening file, maybe wrong format? error: {e}")

    def recorder(self):
        def record(seconds):
            start_time = datetime.datetime.now()
            times = []
            xs = []
            ys = []

            # record for 10 seconds
            print(f"Recording for {seconds} seconds...")
            self.ui.startrecording.setDisabled(True)
            while (datetime.datetime.now() - start_time).total_seconds() <= seconds:
                self.recordstate = True
                times.append((datetime.datetime.now() - start_time).total_seconds())
                xs.append(self.livex[-1])
                ys.append(self.livey[-1])
                sleep(0.01)
            self.recordstate = False
            print("Done recording")
            self.recording = np.column_stack((times, xs, ys))
            self.ui.startrecording.setDisabled(False)
            self.ui.analyserecording.setDisabled(False)

        if self.recordstate:
            print("Already recording.")
            return
        elif self.ui.statustext.text() == 'disconnected':
            print("No balance board connected.")
            return
        elif self.ui.statustext.text() == 'connected':
            recordthread = Thread(target=record, args=(self.ui.recordlength.value(),))
            recordthread.daemon = True
            recordthread.start()
        else:
            print("Unknown error occurred.")

    def playpause(self):
        if not self.playstate:
            self.start_time = datetime.datetime.now() - datetime.timedelta(seconds=self.analysisdata[self.analysisidx][0])
        self.playstate = not self.playstate

    def restart(self):
        self.analysisidx = 0
        self.playstate = False
        self.playpause()
        self.ui.analysisplay.setDisabled(False)
        self.update()

    def slider_changed(self):
        self.start_time = datetime.datetime.now() - datetime.timedelta(seconds=self.analysisdata[self.ui.timeslider.value()-1][0])
        self.ui.widget.line.setData(self.analysisdata[:self.analysisidx, 1],
                                    self.analysisdata[:self.analysisidx, 2])
        self.update()

    def slider_pressed(self):
        self.timer.stop()

    def slider_released(self):
        self.analysisidx = self.ui.timeslider.value()
        self.timer.start(self.interval)
        self.update()

    def switchmode(self):
        if self.mode == 0:  # if mode is live (0), switch to analysis (1)
            self.analysisidx = 0
            self.mode = 1

        elif self.mode == 1:  # if mode is analysis (1), switch to live (0)
            self.mode = 0
        else:
            print("Unknown mode.")
        self.update()

    def analyserecording(self):
        target_frequency = 100
        time = self.recording[:, 0]
        x = self.recording[:, 1]
        y = self.recording[:, 2]
        # normalize time, x and y
        time = time - time[0]
        x = x - np.mean(x)
        y = y - np.mean(y)
        data = np.array([time, x, y]).T

        valid_index = (np.sum(np.isnan(data), axis=1) == 0)
        if np.sum(valid_index) != len(data):
            raise ValueError("Clean NaN values first")

        stato = Stabilogram()
        stato.from_array(array=data, resample_frequency=target_frequency)
        # add time to stato
        stato.time = np.linspace(0, len(stato.signal) / target_frequency, len(stato.signal))

        newdata = np.column_stack((stato.time, stato.signal))
        # round to 2 decimals
        newdata = np.round(newdata, 2)
        self.analysisdata = newdata

        # enable buttons and change mode
        self.ui.analysisplay.setDisabled(False)
        self.ui.saverecording.setDisabled(False)
        self.ui.analysisrestart.setDisabled(False)
        self.ui.timeslider.setDisabled(False)
        self.ui.currenttime.setText(f'{self.analysisdata[self.analysisidx][0]:.2f} s')
        self.ui.timeslider.setMaximum(len(self.analysisdata))
        self.ui.maxtime.setText(f'{self.analysisdata[-1][0]:.2f} s')
        self.ui.analysisapwidget.graph.setRange(xRange=[0, self.analysisdata[-1][0]], yRange=[-115, 115], update=True)
        self.ui.analysismlwidget.graph.setRange(xRange=[0, self.analysisdata[-1][0]], yRange=[-220, 220], update=True)
        self.ui.modes.setCurrentIndex(1)

        # Table view
        features = compute_all_features(stato)
        self.ui.tableWidget.setRowCount(len(features))
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Feature', 'Value'])
        for i, (key, value) in enumerate(features.items()):
            self.ui.tableWidget.setItem(i, 0, frontend.QTableWidgetItem(key))
            self.ui.tableWidget.setItem(i, 1, frontend.QTableWidgetItem(str(value)))
        # set width of columns
        self.ui.tableWidget.setColumnWidth(0, 300)
        self.ui.tableWidget.setColumnWidth(1, 300)

        pass


if __name__ == '__main__':
    plot = STEPviewer(dummy=False)
