# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.checkBoxAddResults = QCheckBox(self.configGroupBox)
        self.checkBoxAddResults.setObjectName(u"checkBoxAddResults")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.checkBoxAddResults)

        self.checkBoxReplaceResults = QCheckBox(self.configGroupBox)
        self.checkBoxReplaceResults.setObjectName(u"checkBoxReplaceResults")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.checkBoxReplaceResults)

        self.label0_2 = QLabel(self.configGroupBox)
        self.label0_2.setObjectName(u"label0_2")
        self.label0_2.setWordWrap(True)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.label0_2)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.checkBoxAddResults.setText(QCoreApplication.translate("ConfigureDialog", u"Add results port", None))
        self.checkBoxReplaceResults.setText(QCoreApplication.translate("ConfigureDialog", u"Replace results port", None))
        self.label0_2.setText(QCoreApplication.translate("ConfigureDialog", u"Select at least one of the add results or replace results port:", None))
    # retranslateUi

