
from PySide6.QtWidgets import QWidget, QVBoxLayout
import EntropyHub as EH
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
        # self.graph.setMouseEnabled(x=False, y=False)
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
        self.setmode('AP')
        self.graph.setMouseEnabled(x=False, y=True)
        self.graph.hideButtons()

    def setmode(self, mode):
        if mode == 'AP':
            self.graph.setRange(xRange=[0, 30], yRange=[-115, 115], update=True)
            self.graph.setTitle('AP')
        if mode == 'ML':
            self.graph.setRange(xRange=[0, 30], yRange=[-220, 220], update=True)
            self.graph.setTitle('ML')


class Entropy(QWidget):
    """
    Widget for displaying entropy data.
    """

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
        self.graph.setLabel('left', 'Suprise', units='??')
        self.graph.setLabel('bottom', 'step', units='tick')
        self.graph.setMouseEnabled(x=False, y=True)
        self.graph.hideButtons()


if __name__ == "__main__":
    ### Test entropy widget ###
    from PySide6.QtWidgets import QApplication
    import numpy as np
    from pyentrp import entropy as ent

    app = QApplication([])
    widget = Entropy()
    data = np.genfromtxt('../QtDesigner/dummyrec.csv', delimiter=' ', skip_header=1)
    data = data[:, 1]
    std = np.std(data)
    # TODO: change window size and tolerance
    sample_entropy = ent.sample_entropy(data, 2, 0.2 * std)
    #sample_entropy2 = EH.SampEn(data, 2, 0.2 * std)
    widget.line.setData(sample_entropy)
    apml = ApMl()
    apml.setmode('ML')
    time = np.linspace(0, 30, len(data))
    apml.line.setData(time, data)
    apml.show()

    widget.show()
    app.exec()
    ##########################
