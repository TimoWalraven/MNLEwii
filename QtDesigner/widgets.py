from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
import pyqtgraph as pg


class Stabilogram(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.graph = pg.PlotWidget(parent)
        self.line = pg.PlotCurveItem(pen=pg.mkPen(color=(0, 0, 255), width=3))
        self.graph.addItem(self.line)
        self.layout.addWidget(self.graph)

        self.graph.setAxisItems({'bottom': pg.AxisItem(orientation='bottom', showValues=True),
                                 'left': pg.AxisItem(orientation='left', showValues=True),
                                 'top': pg.AxisItem(orientation='top', showValues=True),
                                 'right': pg.AxisItem(orientation='right', showValues=True)})
        self.graph.setBackground(None)
        self.graph.showGrid(x=True, y=True)
        self.graph.setRange(xRange=[-220, 220], yRange=[-115, 115], update=True)
        self.graph.setLabel('left', 'AP', units='mm')
        self.graph.setLabel('right', 'AP', units='mm')
        self.graph.setLabel('bottom', 'ML', units='mm')
        self.graph.setAspectLocked(True, 1)
        self.graph.setMouseEnabled(x=False, y=False)
        self.graph.hideButtons()


class ApMl(QWidget):
    """Widget for displaying APML data."""
    def __init__(self, parent=None):
        """Initialize the widget."""
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.graph = pg.PlotWidget()
        self.layout.addWidget(self.graph)
        self.line = pg.PlotCurveItem(pen=pg.mkPen(color=(0, 0, 255), width=3))
        self.graph.addItem(self.line)
        self.layout.addWidget(self.graph)

        self.graph.setBackground(None)
        self.graph.showGrid(y=True)
        self.graph.setLabel('left', 'Sway', units='mm')
        self.graph.setLabel('bottom', 'Time', units='s')
        self.graph.setMouseEnabled(x=False, y=False)
        self.graph.hideButtons()

        self.setmode('AP')

    def setmode(self, mode):
        if mode == 'AP':
            self.graph.setRange(xRange=[0, 30], yRange=[-115, 115], update=True)
            self.graph.setTitle('AP')
        if mode == 'ML':
            self.graph.setRange(xRange=[0, 30], yRange=[-220, 220], update=True)
            self.graph.setTitle('ML')


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    # Create an instance of your custom widget
    custom_widget = ApMl('ML')

    # Show the widget
    custom_widget.show()

    app.exec()
