# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogiRAcfT.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(422, 281)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gbSerialPort = QGroupBox(Dialog)
        self.gbSerialPort.setObjectName(u"gbSerialPort")
        self.gbSerialPort.setGeometry(QRect(10, 0, 401, 61))
        self.cmbPorts = QComboBox(self.gbSerialPort)
        self.cmbPorts.setObjectName(u"cmbPorts")
        self.cmbPorts.setGeometry(QRect(70, 20, 101, 22))
        self.btnConnect = QPushButton(self.gbSerialPort)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setGeometry(QRect(180, 20, 101, 23))
        self.btnDisconnect = QPushButton(self.gbSerialPort)
        self.btnDisconnect.setObjectName(u"btnDisconnect")
        self.btnDisconnect.setGeometry(QRect(290, 20, 101, 23))
        self.lblPortName = QLabel(self.gbSerialPort)
        self.lblPortName.setObjectName(u"lblPortName")
        self.lblPortName.setGeometry(QRect(10, 20, 61, 20))
        self.gbProgressBars = QGroupBox(Dialog)
        self.gbProgressBars.setObjectName(u"gbProgressBars")
        self.gbProgressBars.setGeometry(QRect(10, 70, 311, 201))
        self.pbAI_2 = QProgressBar(self.gbProgressBars)
        self.pbAI_2.setObjectName(u"pbAI_2")
        self.pbAI_2.setGeometry(QRect(40, 80, 201, 16))
        self.pbAI_2.setMaximum(1023)
        self.pbAI_2.setValue(0)
        self.pbAI_2.setAlignment(Qt.AlignCenter)
        self.lblAI_0 = QLabel(self.gbProgressBars)
        self.lblAI_0.setObjectName(u"lblAI_0")
        self.lblAI_0.setGeometry(QRect(10, 10, 21, 31))
        self.lblAI_0.setAlignment(Qt.AlignCenter)
        self.lblAI_2 = QLabel(self.gbProgressBars)
        self.lblAI_2.setObjectName(u"lblAI_2")
        self.lblAI_2.setGeometry(QRect(10, 70, 21, 31))
        self.lblAI_2.setAlignment(Qt.AlignCenter)
        self.pbAI_1 = QProgressBar(self.gbProgressBars)
        self.pbAI_1.setObjectName(u"pbAI_1")
        self.pbAI_1.setGeometry(QRect(40, 50, 201, 16))
        self.pbAI_1.setMaximum(1023)
        self.pbAI_1.setValue(0)
        self.pbAI_1.setAlignment(Qt.AlignCenter)
        self.pbAI_0 = QProgressBar(self.gbProgressBars)
        self.pbAI_0.setObjectName(u"pbAI_0")
        self.pbAI_0.setGeometry(QRect(40, 20, 201, 16))
        self.pbAI_0.setMaximum(1023)
        self.pbAI_0.setValue(0)
        self.pbAI_0.setAlignment(Qt.AlignCenter)
        self.pbAI_3 = QProgressBar(self.gbProgressBars)
        self.pbAI_3.setObjectName(u"pbAI_3")
        self.pbAI_3.setGeometry(QRect(40, 110, 201, 16))
        self.pbAI_3.setMaximum(1023)
        self.pbAI_3.setValue(0)
        self.pbAI_3.setAlignment(Qt.AlignCenter)
        self.lblAI_1 = QLabel(self.gbProgressBars)
        self.lblAI_1.setObjectName(u"lblAI_1")
        self.lblAI_1.setGeometry(QRect(10, 40, 21, 31))
        self.lblAI_1.setAlignment(Qt.AlignCenter)
        self.lblAI_5 = QLabel(self.gbProgressBars)
        self.lblAI_5.setObjectName(u"lblAI_5")
        self.lblAI_5.setGeometry(QRect(10, 160, 21, 31))
        self.lblAI_5.setAlignment(Qt.AlignCenter)
        self.lblAI_3 = QLabel(self.gbProgressBars)
        self.lblAI_3.setObjectName(u"lblAI_3")
        self.lblAI_3.setGeometry(QRect(10, 100, 21, 31))
        self.lblAI_3.setAlignment(Qt.AlignCenter)
        self.pbAI_4 = QProgressBar(self.gbProgressBars)
        self.pbAI_4.setObjectName(u"pbAI_4")
        self.pbAI_4.setGeometry(QRect(40, 140, 201, 16))
        self.pbAI_4.setMaximum(1023)
        self.pbAI_4.setValue(0)
        self.pbAI_4.setAlignment(Qt.AlignCenter)
        self.pbAI_5 = QProgressBar(self.gbProgressBars)
        self.pbAI_5.setObjectName(u"pbAI_5")
        self.pbAI_5.setGeometry(QRect(40, 170, 201, 16))
        self.pbAI_5.setMaximum(1023)
        self.pbAI_5.setValue(0)
        self.pbAI_5.setAlignment(Qt.AlignCenter)
        self.lblAI_4 = QLabel(self.gbProgressBars)
        self.lblAI_4.setObjectName(u"lblAI_4")
        self.lblAI_4.setGeometry(QRect(10, 130, 21, 31))
        self.lblAI_4.setAlignment(Qt.AlignCenter)
        self.leAI_0 = QLineEdit(self.gbProgressBars)
        self.leAI_0.setObjectName(u"leAI_0")
        self.leAI_0.setGeometry(QRect(250, 20, 51, 16))
        self.leAI_0.setAlignment(Qt.AlignCenter)
        self.leAI_0.setReadOnly(True)
        self.leAI_1 = QLineEdit(self.gbProgressBars)
        self.leAI_1.setObjectName(u"leAI_1")
        self.leAI_1.setGeometry(QRect(250, 50, 51, 16))
        self.leAI_1.setAlignment(Qt.AlignCenter)
        self.leAI_1.setReadOnly(True)
        self.leAI_2 = QLineEdit(self.gbProgressBars)
        self.leAI_2.setObjectName(u"leAI_2")
        self.leAI_2.setGeometry(QRect(250, 80, 51, 16))
        self.leAI_2.setAlignment(Qt.AlignCenter)
        self.leAI_2.setReadOnly(True)
        self.leAI_3 = QLineEdit(self.gbProgressBars)
        self.leAI_3.setObjectName(u"leAI_3")
        self.leAI_3.setGeometry(QRect(250, 110, 51, 16))
        self.leAI_3.setAlignment(Qt.AlignCenter)
        self.leAI_3.setReadOnly(True)
        self.leAI_4 = QLineEdit(self.gbProgressBars)
        self.leAI_4.setObjectName(u"leAI_4")
        self.leAI_4.setGeometry(QRect(250, 140, 51, 16))
        self.leAI_4.setAlignment(Qt.AlignCenter)
        self.leAI_4.setReadOnly(True)
        self.leAI_5 = QLineEdit(self.gbProgressBars)
        self.leAI_5.setObjectName(u"leAI_5")
        self.leAI_5.setGeometry(QRect(250, 170, 51, 16))
        self.leAI_5.setAlignment(Qt.AlignCenter)
        self.leAI_5.setReadOnly(True)
        self.gbLED = QGroupBox(Dialog)
        self.gbLED.setObjectName(u"gbLED")
        self.gbLED.setGeometry(QRect(330, 70, 81, 201))
        self.sldPWM = QSlider(self.gbLED)
        self.sldPWM.setObjectName(u"sldPWM")
        self.sldPWM.setGeometry(QRect(30, 40, 22, 121))
        self.sldPWM.setMaximum(255)
        self.sldPWM.setOrientation(Qt.Vertical)
        self.sldPWM.setInvertedAppearance(False)
        self.sldPWM.setInvertedControls(False)
        self.sldPWM.setTickPosition(QSlider.TicksBelow)
        self.sldPWM.setTickInterval(10)
        self.lePwm = QLineEdit(self.gbLED)
        self.lePwm.setObjectName(u"lePwm")
        self.lePwm.setGeometry(QRect(10, 20, 61, 16))
        self.lePwm.setAlignment(Qt.AlignCenter)
        self.lePwm.setReadOnly(True)
        self.btnUpdatePwm = QPushButton(self.gbLED)
        self.btnUpdatePwm.setObjectName(u"btnUpdatePwm")
        self.btnUpdatePwm.setGeometry(QRect(10, 170, 61, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Serial Monitor", None))
        self.gbSerialPort.setTitle(QCoreApplication.translate("Dialog", u"Serial Port", None))
        self.btnConnect.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.btnDisconnect.setText(QCoreApplication.translate("Dialog", u"Disconnect", None))
        self.lblPortName.setText(QCoreApplication.translate("Dialog", u"Port Name: ", None))
        self.gbProgressBars.setTitle(QCoreApplication.translate("Dialog", u"Analog Inputs", None))
        self.lblAI_0.setText(QCoreApplication.translate("Dialog", u"[0]", None))
        self.lblAI_2.setText(QCoreApplication.translate("Dialog", u"[2]", None))
        self.lblAI_1.setText(QCoreApplication.translate("Dialog", u"[1]", None))
        self.lblAI_5.setText(QCoreApplication.translate("Dialog", u"[5]", None))
        self.lblAI_3.setText(QCoreApplication.translate("Dialog", u"[3]", None))
        self.lblAI_4.setText(QCoreApplication.translate("Dialog", u"[4]", None))
        self.gbLED.setTitle(QCoreApplication.translate("Dialog", u"Onboard LED", None))
        self.btnUpdatePwm.setText(QCoreApplication.translate("Dialog", u"Update", None))
    # retranslateUi

