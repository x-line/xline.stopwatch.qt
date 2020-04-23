# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addLap.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_addLap(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Add Device")
        #self.resize(400, 300)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(34, 30, 111, 16))
        self.comboBox = QComboBox(self)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 22, 201, 32))
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 62, 121, 16))
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(165, 60, 113, 21))
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(166, 95, 101, 16))
        self.radioButton = QRadioButton(self)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(40, 150, 100, 20))
        self.radioButton_2 = QRadioButton(self)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(40, 208, 100, 20))
        self.radioButton_3 = QRadioButton(self)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(40, 176, 100, 20))
        self.radioButton_4 = QRadioButton(self)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(40, 238, 100, 20))
        self.dateTimeEdit = QDateTimeEdit(self)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(180, 176, 194, 22))
        self.dateTimeEdit_2 = QDateTimeEdit(self)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setGeometry(QRect(180, 238, 194, 22))
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 290, 113, 32))
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 290, 113, 32))

        self.retranslateUi(self)
        self.exec_()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, addLap):
        addLap.setWindowTitle(QCoreApplication.translate("addLap", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("addLap", u"Task Description : ", None))
        self.label_2.setText(QCoreApplication.translate("addLap", u"Enter the duration : ", None))
        self.label_3.setText("")
        self.radioButton.setText(QCoreApplication.translate("addLap", u"Ending Now", None))
        self.radioButton_2.setText(QCoreApplication.translate("addLap", u"Starting Now", None))
        self.radioButton_3.setText(QCoreApplication.translate("addLap", u"Ending", None))
        self.radioButton_4.setText(QCoreApplication.translate("addLap", u"Starting At", None))
        self.pushButton.setText(QCoreApplication.translate("addLap", u"Record", None))
        self.pushButton_2.setText(QCoreApplication.translate("addLap", u"Cancel", None))
    # retranslateUi

