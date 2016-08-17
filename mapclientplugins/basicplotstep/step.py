
'''
MAP Client Plugin Step
'''
import os
import json

from PySide import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.basicplotstep.configuredialog import ConfigureDialog
from mapclientplugins.basicplotstep.ui.reviewwidget import ReviewWidget


class BasicPlotStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(BasicPlotStep, self).__init__('Basic Plot', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Model Viewer'
        # Add any other initialisation code here:
        self._icon =  QtGui.QImage(':/basicplotstep/images/model-viewer.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#plot_settings'))
        self._datasets_port = ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                               'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                               'http://physiomeproject.org/workflow/1.0/rdf-schema#plot_datasets')
        # Port data:
        self._portPlotSettings = None
        self._portAddResults = None
        self._portReplaceResults = None
        # Config:
        self._config = {}
        self._config['identifier'] = ''
        self._config['add_results'] = False
        self._config['replace_results'] = False

        self._widget = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        if self._widget is None:
            self._widget = ReviewWidget()
            self._widget.registerDoneCallback(self._doneExecution)

        self._widget.setPlotSettings(self._portPlotSettings)
        self._widget.addResults(self._portAddResults)
        self._widget.replaceResults(self._portReplaceResults)

        self._setCurrentWidget(self._widget)
        # self._doneExecution()

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self._portPlotSettings = dataIn
        elif index == 1 and self._config['add_results']:
            self._portAddResults = dataIn
        elif index == 1 and not self._config['add_results']:
            self._portReplaceResults = dataIn
        else:
            self._portReplaceResults = dataIn

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog(QtGui.QApplication.activeWindow().currentWidget())
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._setupPorts()
        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.
        '''
        self._config.update(json.loads(string))
        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._setupPorts()
        self._configured = d.validate()

    def _setupPorts(self):
        """
        Make the ports for the step match the configuration.

        :return:
        """
        len_ports = len(self._ports)
        target_ports_len = 1
        target_ports_len += 1 if self._config['replace_results'] else 0
        target_ports_len += 1 if self._config['add_results'] else 0
        while len_ports < target_ports_len:
            self.addPort(self._datasets_port)
            len_ports = len(self._ports)
        while len_ports > target_ports_len:
            self._ports.pop()
            len_ports = len(self._ports)



