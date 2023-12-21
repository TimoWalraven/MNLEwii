import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QShortcut, QKeySequence
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
        try:
            import configparser
            config = configparser.ConfigParser()
            self.config = config.read('STEPconfig.ini')
            self.config = {
                "practitioner": config['GENERAL']['practitioner'],
                "url": config['RESEARCHDRIVE']['url'],
                "username": config['RESEARCHDRIVE']['username'],
                "password": config['RESEARCHDRIVE']['password']
            }
            print(self.config)
        except Exception as e:
            self.config = {
                "practitioner": "unknown",
                "url": None,
                "username": None,
                "password": None
            }
        self.ui.modes.currentChanged.connect(self.switchmode)
        self.mode = self.ui.modes.currentIndex()

        self.livex = []
        self.livey = []
        self.analysisdata = np.array([])

        self.idx = 0

        self.display = False

        # Live mode variables
        self.status = 'disconnected'
        self.ui.statustext.setText(f"initializing...")

        self.com_list = []
        self.com_port_selected = None

        self.recording = []
        self.recordinginfo = {
            "date": "",
            "time": "",
            "duration": "",
            "stance": "",
            "eyes": "",
            "identifier": "",
            "age": "",
            "height": "",
            "weight": "",
            "condition": "",
            "medication": "",
            "fallhistory": "",
            "notes": ""
        }
        self.recordstate = False

        if dummy:
            self.dummyrec = np.genfromtxt('dummyrec.csv', delimiter=' ')[1:]
            self.livex = [i[1] for i in self.dummyrec]
            self.livey = [i[2] for i in self.dummyrec]
            self.recording = self.dummyrec
            self.recordinginfo = {
                "date": datetime.datetime.now().date(),
                "time": datetime.datetime.now().time(),
                "duration": "10 s",
                "stance": "double legged",
                "eyes": "open",
                "identifier": "dummyperson1",
                "age": "50",
                "height": "180 cm",
                "weight": "83 kg",
                "condition": "",
                "medication": "",
                "fallhistory": "",
                "notes": ""
            }

        # Analysis mode variables
        self.analysisidx = 0  # index of current measurement
        self.playstate = False  # state of the play button

        # Live mode setup
        # Toolbar: from left to right
        self.ui.startrecording.clicked.connect(self.recorder)

        self.ui.analyserecording.clicked.connect(self.analyserecording)
        if not dummy:
            self.ui.analyserecording.setDisabled(True)

        # Patient info
        self.ui.identifierreload.clicked.connect(self.randompatient)

        # Plots
        self.ui.liveapwidget.setmode('AP')
        self.ui.livemlwidget.setmode('ML')

        # Analysis mode setup
        # shortcuts
        #TODO: investigate why this prints space as well
        self.shortcut = QShortcut(QKeySequence("Space"), self.win)
        print(self.shortcut.key().toString())
        self.shortcut.activated.connect(self.playpause)
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
        # Slider max value
        self.ui.maxtime.setText(f'--')
        # Restart button
        self.ui.analysisrestart.clicked.connect(self.restart)
        self.ui.analysisrestart.setDisabled(True)
        # Save button
        self.ui.saverecording.clicked.connect(self.saverecording)  # save button
        self.ui.saverecording.setDisabled(True)

        # Patient info
        self.ui.identifierreload_2.clicked.connect(self.randompatient)

        # Plots
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
        while True:
            if self.mode == 0:
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
                print("Serial port closed, trying to reconnect...")

    def update(self):

        # Live mode
        # TODO: add correct time to live plot
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
        # TODO: if initialized in mode 1, doesnt connect
        elif self.mode == 1:
            if len(self.analysisdata) > 1:
                self.ui.currenttime.setText(f'{self.analysisdata[self.analysisidx][0]:.2f} s')
                time = self.analysisdata[:self.analysisidx, 0]
                x = self.analysisdata[:self.analysisidx, 1]
                y = self.analysisdata[:self.analysisidx, 2]
                self.ui.analysisstabilogramwidget.line.setData(x, y)
                self.ui.analysisapwidget.line.setData(time, y)
                self.ui.analysismlwidget.line.setData(time, x)
                # update plot
                if self.playstate:
                    self.ui.timeslider.setValue(self.analysisidx)
                if self.playstate and self.analysisidx < len(self.analysisdata) - 1:
                    self.analysisidx += 1

                elif self.playstate and self.analysisidx >= len(self.analysisdata) - 1:
                    self.playstate = False
                    self.ui.analysisplay.setDisabled(True)
        QApplication.processEvents()

    def saverecording(self):
        if len(self.recording) < 1:
            print("No recording found.")
            return
        elif self.recordstate:
            print("Recording in progress, please wait for recording to finish.")
            return
        filename = QFileDialog.getSaveFileName(self.win, 'Save File', '', 'Excel Files (*.xlsx)')
        import pandas as pd
        data_df = pd.DataFrame(self.recording, columns=['time', 'x', 'y'])
        data_df['time'] = data_df['time'].round(2)
        data_df['x'] = data_df['x'].round(4)
        data_df['y'] = data_df['y'].round(4)

        metadata_df = pd.DataFrame(self.recordinginfo, index=[0])
        metadata_df['age'] = metadata_df['age'].astype(str)
        metadata_df['height'] = metadata_df['height'].astype(str)
        metadata_df['weight'] = metadata_df['weight'].astype(str)
        metadata_df['duration'] = metadata_df['duration'].astype(str)
        metadata_df['date'] = metadata_df['date'].astype(str)
        metadata_df['time'] = metadata_df['time'].astype(str)
        metadata_df['identifier'] = metadata_df['identifier'].astype(str)
        metadata_df['stance'] = metadata_df['stance'].astype(str)
        metadata_df['eyes'] = metadata_df['eyes'].astype(str)
        metadata_df['condition'] = metadata_df['condition'].astype(str)
        metadata_df['medication'] = metadata_df['medication'].astype(str)
        metadata_df['fallhistory'] = metadata_df['fallhistory'].astype(str)
        metadata_df['notes'] = metadata_df['notes'].astype(str)
        metadata_df['practitioner'] = self.config['practitioner']

        succes = False
        try:
            print(f"Saving file to {filename[0]}")
            with pd.ExcelWriter(f'{filename[0]}', engine='xlsxwriter' , mode='w') as writer:
                data_df.to_excel(writer, sheet_name='Data', index=False)
                metadata_df.to_excel(writer, sheet_name='Metadata', index=False)
                print("File successfully saved locally.")
                succes = True
        except Exception as e:
            print(f"Error while saving file: {e}")
            return

        if succes:
            try:
                if self.ui.contribute.isChecked():
                    self.sendtoresearchdrive(filename[0])
                    print("File successfully saved on ResearchDrive.")
            except Exception as e:
                print(f"Error while uploading file: {e}")
                return

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
            self.ui.timeslider.setMaximum(len(self.analysisdata) - 1)
            self.ui.maxtime.setText(f'{self.analysisdata[-1][0]:.2f} s')

            # set range of plot by time
            self.ui.analysisapwidget.graph.setRange(xRange=[0, self.analysisdata[-1][0]], yRange=[-115, 115],
                                                    update=True)
            self.ui.analysismlwidget.graph.setRange(xRange=[0, self.analysisdata[-1][0]], yRange=[-220, 220],
                                                    update=True)

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
            try:
                while (datetime.datetime.now() - start_time).total_seconds() <= seconds:
                    self.recordstate = True
                    times.append((datetime.datetime.now() - start_time).total_seconds())
                    xs.append(self.livex[-1])
                    ys.append(self.livey[-1])
                    sleep(0.01)
            except Exception as e:
                print(f"Error while recording: {e}")
                self.recordstate = False
                self.ui.startrecording.setDisabled(False)
                return

            self.recordstate = False
            print("Done recording")
            self.recording = np.column_stack((times, xs, ys))
            self.recordinginfo = {"date": start_time.date(),
                                  "time": start_time.time(),
                                  "duration": self.ui.recordlength.value(),
                                  "stance": self.ui.stanceselect.currentText(),
                                  "eyes": self.ui.eyeselect.currentText(),
                                  "identifier": self.ui.identifierselect.currentText(),
                                  "age": self.ui.ageselect.value(),
                                  "height": self.ui.heightselect.value(),
                                  "weight": self.ui.weightselect.value(),
                                  "condition": self.ui.conditionselect.currentText(),
                                  "medication": self.ui.medicationselect.currentText(),
                                  "fallhistory": self.ui.fallhistoryselect.currentText(),
                                  "notes": self.ui.notesedit.toPlainText()}

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
            # check if recording was successful

        else:
            print("Unknown error occurred.")

    def playpause(self):
        if self.mode == 1 and len(self.analysisdata) > 1:
            if not self.playstate:
                self.start_time = datetime.datetime.now() - datetime.timedelta(
                    seconds=self.analysisdata[self.analysisidx][0])
            self.playstate = not self.playstate

    def restart(self):
        self.analysisidx = 0
        self.playstate = False
        self.playpause()
        self.ui.analysisplay.setDisabled(False)
        self.update()

    def slider_changed(self):
        # TODO: graphs do not update when slider is moved
        self.start_time = datetime.datetime.now() - datetime.timedelta(
            seconds=self.analysisdata[self.ui.timeslider.value() - 1][0])
        self.ui.currenttime.setText(f'{self.analysisdata[self.ui.timeslider.value()][0]:.2f} s')
        self.ui.analysisstabilogramwidget.line.setData(self.analysisdata[:self.ui.timeslider.value(), 1],
                                                       self.analysisdata[:self.ui.timeslider.value(), 2])
        self.ui.analysisapwidget.line.setData(self.analysisdata[:self.ui.timeslider.value(), 0],
                                              self.analysisdata[:self.ui.timeslider.value(), 2])
        self.ui.analysismlwidget.line.setData(self.analysisdata[:self.ui.timeslider.value(), 0],
                                              self.analysisdata[:self.ui.timeslider.value(), 1])
        # self.update()

    def slider_pressed(self):
        self.timer.stop()
        self.playstate = False

    def slider_released(self):
        self.analysisidx = self.ui.timeslider.value()
        self.timer.start(self.interval)
        self.update()
        if self.analysisidx != len(self.analysisdata):
            self.ui.analysisplay.setDisabled(False)

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
        self.ui.timeslider.setMaximum(len(self.analysisdata) - 1)
        self.ui.maxtime.setText(f'{self.analysisdata[-1][0]:.2f} s')
        self.ui.analysisapwidget.graph.setRange(xRange=[0, self.analysisdata[-1][0]], yRange=[-115, 115], update=True)
        self.ui.analysismlwidget.graph.setRange(xRange=[0, self.analysisdata[-1][0]], yRange=[-220, 220], update=True)
        self.ui.modes.setCurrentIndex(1)

        # recording info
        # TODO: add hash from recording as unique identifier
        self.updatepatientinfo()

        """# Table view
        features = compute_all_features(stato)
        self.ui.tableWidget.setRowCount(len(features))
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Feature', 'Value'])
        for i, (key, value) in enumerate(features.items()):
            self.ui.tableWidget.setItem(i, 0, frontend.QTableWidgetItem(key))
            self.ui.tableWidget.setItem(i, 1, frontend.QTableWidgetItem(str(value)))
        # set width of columns
        self.ui.tableWidget.setColumnWidth(0, 300)
        self.ui.tableWidget.setColumnWidth(1, 300)"""

        pass

    def updatepatientinfo(self, info=None):

        if not info:
            self.ui.testinfolabel_2.setText(
                f"Test info | {datetime.datetime.now().strftime('%d-%m-%y')} | {datetime.datetime.now().strftime('%H:%M:%S')}")
            self.ui.maxtime.setText(f"{np.max(self.recording[:, 0]):.2f} s")
            self.ui.stanceselect_2.setCurrentText(self.ui.stanceselect.currentText())
            self.ui.identifierselect_2.setText(self.ui.identifierselect.text())
            self.ui.eyeselect_2.setCurrentText(self.ui.eyeselect.currentText())
            self.ui.ageselect_2.setValue(self.ui.ageselect.value())
            self.ui.heightselect_2.setValue(self.ui.heightselect.value())
            self.ui.weightselect_2.setValue(self.ui.weightselect.value())
            self.ui.conditionselect_2.setCurrentText(self.ui.conditionselect.currentText())
            self.ui.medicationselect_2.setCurrentText(self.ui.medicationselect.currentText())
            self.ui.fallhistoryselect_2.setCurrentText(self.ui.fallhistoryselect.currentText())
            self.ui.notesedit_2.setPlainText(self.ui.notesedit.toPlainText())

        elif isinstance(info, dict):
            try:
                self.ui.testinfolabel_2.setText(f"Test info | {info['date']} | {info['time']}")
                self.ui.maxtime.setText(f"{info['duration']} s")
                self.ui.stanceselect_2.setCurrentText(info['stance'])
                self.ui.eyeselect_2.setCurrentText(info['eyes'])
                self.ui.identifierselect_2.setText(info['identifier'])
                self.ui.ageselect_2.setValue(info['age'])
                self.ui.heightselect_2.setValue(info['height'])
                self.ui.weightselect_2.setValue(info['weight'])
                self.ui.conditionselect_2.setCurrentText(info['condition'])
                self.ui.medicationselect_2.setCurrentText(info['medication'])
                self.ui.fallhistoryselect_2.setCurrentText(info['fallhistory'])
                self.ui.notesedit_2.setPlainText(info['notes'])
            except Exception as e:
                print(f"Error while updating patient info: {e}")

        else:
            print("info format unsupported.")

        pass

    def sendtoresearchdrive(self, filepath: str):
        if None in (self.config['url'], self.config['username'], self.config['password']):
            print("No url, username or password found: please enter your credentials in the config file.")
        else:
            print("Uploading file to research drive..")
            import subprocess
            url = self.config['url']
            username = self.config['username']
            password = self.config['password']
            filename = filepath.split('/')[-1]
            command = f'curl -T {filepath} -u "{username}:{password}" {url}{filename}'
            try:
                subprocess.run(command, shell=False)
                print("File uploaded successfully.")
            except Exception as e:
                print(f"Error while uploading file: {e}")
            pass

    def randompatient(self):
        import random
        import string
        self.recordinginfo['identifier'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        self.updatepatientinfo(self.recordinginfo)

if __name__ == '__main__':
    plot = STEPviewer(dummy=True)


