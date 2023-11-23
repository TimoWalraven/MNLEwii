from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import frontend


def update():
    return


ui = frontend.Ui_MainWindow()
app = QApplication([])
win = QMainWindow()
ui.setupUi(win)
ui.liveapwidget.setmode('AP')
ui.livemlwidget.setmode('ML')

# add timer to update plots
timer = QTimer()
timer.timeout.connect(update)
timer.start(10)


win.show()
app.exec()
