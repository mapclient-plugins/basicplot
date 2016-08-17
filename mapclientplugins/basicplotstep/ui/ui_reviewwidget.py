# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\reviewwidget.ui'
#
# Created: Thu Mar 17 02:39:36 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ReviewWidget(object):
    def setupUi(self, ReviewWidget):
        ReviewWidget.setObjectName("ReviewWidget")
        ReviewWidget.resize(592, 467)
        self.horizontalLayout = QtGui.QHBoxLayout(ReviewWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(ReviewWidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonClear = QtGui.QPushButton(self.groupBox)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.verticalLayout.addWidget(self.pushButtonClear)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButtonDone = QtGui.QPushButton(self.groupBox)
        self.pushButtonDone.setObjectName("pushButtonDone")
        self.verticalLayout.addWidget(self.pushButtonDone)
        self.horizontalLayout.addWidget(self.groupBox)
        self.widgetPlot = MatplotlibWidget(ReviewWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetPlot.sizePolicy().hasHeightForWidth())
        self.widgetPlot.setSizePolicy(sizePolicy)
        self.widgetPlot.setObjectName("widgetPlot")
        self.horizontalLayout.addWidget(self.widgetPlot)

        self.retranslateUi(ReviewWidget)
        QtCore.QMetaObject.connectSlotsByName(ReviewWidget)

    def retranslateUi(self, ReviewWidget):
        ReviewWidget.setWindowTitle(QtGui.QApplication.translate("ReviewWidget", "Review", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClear.setText(QtGui.QApplication.translate("ReviewWidget", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDone.setText(QtGui.QApplication.translate("ReviewWidget", "Done", None, QtGui.QApplication.UnicodeUTF8))

from mapclientplugins.basicplotstep.ui.matplotlibwidget import MatplotlibWidget
