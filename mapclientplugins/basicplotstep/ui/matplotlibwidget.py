from PySide6 import QtWidgets

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class MatplotlibWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self._figure = Figure()
        self._canvas = FigureCanvas(self._figure)
        # self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(self.toolbar)
        layout.addWidget(self._canvas)
        self.setLayout(layout)

    def getFigure(self):
        return self._figure

    def draw(self):
        self._figure.canvas.draw()

    def clear(self):
        self._figure.clear()
