import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QFileDialog, QSpinBox, \
    QToolBox, QToolBar
from PySide6.QtCore import QTimer, QSize
import pyqtgraph as pg
from threading import Thread
import serial
from serial.tools import list_ports
import datetime
from time import sleep


class STEPviewer:

    def __init__(self):
        # connection parameters
        self.com_list = []
        self.com_port_selected = None

        # data
        self.display = True
        self.recording = []
        self.recordstate = False
        self.x = []
        self.y = []

        self.app = QApplication.instance()  # checks if QApplication already exists
        if not self.app:  # create QApplication if it doesn't exist
            self.app = QApplication(sys.argv)

        self.window = QWidget()
        self.layout = QVBoxLayout()

        self.win = pg.plot()
        self.line = pg.PlotCurveItem(pen=pg.mkPen(color=(0, 0, 255), width=3))
        self.win.addItem(self.line)
        self.layout.addWidget(self.win)

        self.win.setBackground('w')
        self.win.showGrid(x=True, y=True)
        self.win.setXRange(-220, 220)
        self.win.setYRange(-115, 115)
        self.win.setLabel('left', 'Y', units='mm')
        self.win.setLabel('bottom', 'X', units='mm')
        self.win.setTitle('STEP')
        self.win.setAspectLocked(True)
        self.win.setMouseEnabled(x=False, y=False)
        self.win.hideButtons()

        # toolbar to select mode
        self.mode_toolbar = QToolBar("Toolbar to select mode")
        self.mode_toolbar.setIconSize(QSize(64, 20))
        self.layout.addWidget(self.mode_toolbar)

        self.mode_toolbar_action = QAction("Display", self.mode_toolbar)
        self.mode_toolbar.addAction(self.mode_toolbar_action)

        # add dropdown for com port selection
        self.com_port = QComboBox()
        self.com_port.addItems(self.com_list)
        self.layout.addWidget(self.com_port)

        # add spin box for recording time
        self.record_time = QSpinBox()
        self.record_time.setMinimum(1)
        self.record_time.setMaximum(60)
        self.record_time.setValue(10)
        self.record_time.setSuffix(" s")
        self.layout.addWidget(self.record_time)

        # add record button
        self.record_button = QPushButton("Make recording")
        self.record_button.clicked.connect(self.recorder)
        self.layout.addWidget(self.record_button)

        # add save button
        self.save_button = QPushButton("Save recording")
        self.save_button.clicked.connect(self.saverecording)
        self.layout.addWidget(self.save_button)

        """self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play)
        self.layout.addWidget(self.play_button)

        # Add Pause button
        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause)
        self.layout.addWidget(self.pause_button)

        # Add Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(len(self.x) - 1)
        self.slider.valueChanged.connect(self.slider_changed)
        self.layout.addWidget(self.slider)

        self.time_label = QLabel("Elapsed Time: 0 s")
        self.layout.addWidget(self.time_label)"""

        self.window.setLayout(self.layout)
        self.window.show()
        print("GUI initialized.")

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
        if self.com_port.currentText() not in self.com_list:
            self.com_port.clear()
            self.com_port.addItems(self.com_list)

    def read_from_serial(self):
        while True:
            if self.com_port_selected != self.com_port.currentText() and self.com_port.currentText() in self.com_list:
                self.com_port_selected = self.com_port.currentText()
                print(f'com port selected: {self.com_port_selected}')
            if self.com_port_selected is not None:
                try:
                    with serial.Serial(self.com_port_selected, 115200, timeout=1) as ser:
                        print(f"Serial port {ser.name} successfully opened.")
                        line = ''
                        while self.com_port_selected == self.com_port.currentText():
                            incoming = ser.readline().decode()  # Todo: rrr
                            if incoming and incoming != '':
                                line += incoming[1:-2]
                                self.x.append(float(line.split(', ')[0]))
                                self.y.append(float(line.split(', ')[1]))
                                line = ''
                                if len(self.x) > 30:
                                    self.x.pop(0)
                                    self.y.pop(0)
                            else:
                                continue

                except serial.SerialException as e:
                    print(f"An error occurred: {e} \n Trying to reconnect...")
                    sleep(1)

    def update(self):
        self.line.setData(self.x, self.y)
        self.update_com()

        # Update the record button color
        if self.recordstate and self.record_button.styleSheet() != "background-color: red":
            self.record_button.setStyleSheet("background-color: red")
        elif not self.recordstate and self.record_button.styleSheet() != "background-color: none":
            self.record_button.setStyleSheet("background-color: none")

        """# Disconnect the slider to prevent a feedback loop
        self.slider.valueChanged.disconnect(self.slider_changed)

        # Update the slider position
        self.slider.setValue(self.idx)

        # Reconnect the slider
        self.slider.valueChanged.connect(self.slider_changed)

        # Update elapsed time
        if self.idx < len(self.time):
            elapsed_time = self.time[self.idx] - self.start_time
            self.time_label.setText(f"Elapsed Time: {elapsed_time:.2f} s")"""

        QApplication.processEvents()

    def saverecording(self):
        if not self.recording:
            print("No recording found.")
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
            print("Recording...")
            while (datetime.datetime.now() - start_time).total_seconds() <= self.record_time.value():
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
            self.recording = data

        recordthread = Thread(target=record, args=(10,))
        recordthread.daemon = True
        recordthread.start()

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
    plot = STEPviewer()

