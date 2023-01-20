from PySide6 import QtWidgets

from mapclientplugins.basicplotstep.ui.ui_reviewwidget import Ui_ReviewWidget

colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k']


class ReviewWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ReviewWidget, self).__init__(parent)
        self._ui = Ui_ReviewWidget()
        self._ui.setupUi(self)
        self._doneCallback = None
        self._segmentation_init = False
        self._colour_index = 0

        fig = self._ui.widgetPlot.getFigure()
        self._plot = fig.add_subplot(111)
        self._settings = None

        self._replace_datasets = {}

        self._makeConnections()

    def _makeConnections(self):
        self._ui.pushButtonClear.clicked.connect(self._clearClicked)
        self._ui.pushButtonDone.clicked.connect(self._doneClicked)

    def _resetPlotSettings(self):
        if 'xlabel' in self._settings:
            self._plot.set_xlabel(self._settings['xlabel'])
        if 'ylabel' in self._settings:
            self._plot.set_ylabel(self._settings['ylabel'])
        if 'xlim' in self._settings:
            self._plot.set_xlim(self._settings['xlim'])
        if 'ylim' in self._settings:
            self._plot.set_ylim(self._settings['ylim'])

    def registerDoneCallback(self, cb):
        self._doneCallback = cb

    def _clearClicked(self):
        self._segmentation_init = False
        self._colour_index = 0
        self._replace_datasets = {}
        self._plot.cla()
        self._resetPlotSettings()
        self._ui.widgetPlot.draw()

    def _doneClicked(self):
        self._doneCallback()

    def setPlotSettings(self, settings):
        self._settings = settings
        self._resetPlotSettings()

    def replaceResults(self, results):

        for key in results:
            if key in self._replace_datasets:
                self._plot.lines.remove(self._replace_datasets[key][0])

            dataset = results[key]
            marker = 'ko'
            if "marker" in dataset and dataset["marker"]:
                marker = dataset["marker"]
            self._replace_datasets[key] = self._plot.plot(dataset["x"], dataset["y"], marker)

        self._ui.widgetPlot.draw()

    def addResults(self, results):

        for key in results:
            dataset = results[key]
            label_text = ''
            if "label" in dataset and dataset["label"]:
                label_text = dataset["label"]
            marker = ''
            if "marker" in dataset and dataset["marker"]:
                marker = dataset["marker"]
            self._plot.plot(dataset["x"], dataset["y"], colours[self._colour_index] + marker, label=label_text)

        handles, labels = self._plot.get_legend_handles_labels()
        self._plot.legend(handles, labels, loc=0)
        self._ui.widgetPlot.draw()

        self._colour_index += 1
        if self._colour_index == len(colours):
            self._colour_index = 0
