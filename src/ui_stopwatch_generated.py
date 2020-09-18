# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_stopwatch.ui'
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


class Ui_Stopwatch(object):
    def setupUi(self, Stopwatch):
        if not Stopwatch.objectName():
            Stopwatch.setObjectName(u"Stopwatch")
        Stopwatch.resize(500, 450)
        Stopwatch.setMinimumSize(QSize(500, 450))
        Stopwatch.setMaximumSize(QSize(500, 450))
        self.label = QLabel(Stopwatch)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 131, 31))
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label_2 = QLabel(Stopwatch)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(22, 87, 91, 16))
        self.cboPeriod = QComboBox(Stopwatch)
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.setObjectName(u"cboPeriod")
        self.cboPeriod.setGeometry(QRect(17, 100, 221, 32))
        self.label_3 = QLabel(Stopwatch)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(23, 372, 131, 16))
        self.btnStart = QPushButton(Stopwatch)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(19, 400, 110, 32))
        self.btnAddLap = QPushButton(Stopwatch)
        self.btnAddLap.setObjectName(u"btnAddLap")
        self.btnAddLap.setGeometry(QRect(257, 400, 110, 32))
        self.btnDeleteTimer = QPushButton(Stopwatch)
        self.btnDeleteTimer.setObjectName(u"btnDeleteTimer")
        self.btnDeleteTimer.setGeometry(QRect(369, 400, 110, 32))
        self.cboTasks = QComboBox(Stopwatch)
        self.cboTasks.setObjectName(u"cboTasks")
        self.cboTasks.setEnabled(True)
        self.cboTasks.setGeometry(QRect(157, 365, 290, 32))
        self.cboTasks.setEditable(True)
        self.dtFromFilter = QDateTimeEdit(Stopwatch)
        self.dtFromFilter.setObjectName(u"dtFromFilter")
        self.dtFromFilter.setGeometry(QRect(320, 75, 151, 22))
        self.dtToFilter = QDateTimeEdit(Stopwatch)
        self.dtToFilter.setObjectName(u"dtToFilter")
        self.dtToFilter.setGeometry(QRect(320, 100, 151, 22))
        self.lblFromFilter = QLabel(Stopwatch)
        self.lblFromFilter.setObjectName(u"lblFromFilter")
        self.lblFromFilter.setGeometry(QRect(275, 80, 41, 16))
        self.label_5 = QLabel(Stopwatch)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(276, 100, 41, 16))
        self.listTimers = QListWidget(Stopwatch)
        self.listTimers.setObjectName(u"listTimers")
        self.listTimers.setGeometry(QRect(22, 136, 451, 221))
        self.btnPencil = QPushButton(Stopwatch)
        self.btnPencil.setObjectName(u"btnPencil")
        self.btnPencil.setGeometry(QRect(438, 366, 40, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPencil.sizePolicy().hasHeightForWidth())
        self.btnPencil.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(20)
        self.btnPencil.setFont(font1)
        self.btnPencil.setIconSize(QSize(16, 16))
        self.btnPencil.setFlat(False)

        self.retranslateUi(Stopwatch)

        QMetaObject.connectSlotsByName(Stopwatch)
    # setupUi

    def retranslateUi(self, Stopwatch):
        Stopwatch.setWindowTitle(QCoreApplication.translate("Stopwatch", u"Form", None))
        self.label.setText(QCoreApplication.translate("Stopwatch", u"Stopwatch", None))
        self.label_2.setText(QCoreApplication.translate("Stopwatch", u"Show Timers:", None))
        self.cboPeriod.setItemText(0, QCoreApplication.translate("Stopwatch", u"Total", None))
        self.cboPeriod.setItemText(1, QCoreApplication.translate("Stopwatch", u"Last Lap", None))
        self.cboPeriod.setItemText(2, QCoreApplication.translate("Stopwatch", u"Today", None))
        self.cboPeriod.setItemText(3, QCoreApplication.translate("Stopwatch", u"This Week", None))
        self.cboPeriod.setItemText(4, QCoreApplication.translate("Stopwatch", u"Workweek Average", None))
        self.cboPeriod.setItemText(5, QCoreApplication.translate("Stopwatch", u"This Month", None))
        self.cboPeriod.setItemText(6, QCoreApplication.translate("Stopwatch", u"Monthly Average", None))
        self.cboPeriod.setItemText(7, QCoreApplication.translate("Stopwatch", u"Yesterday", None))
        self.cboPeriod.setItemText(8, QCoreApplication.translate("Stopwatch", u"Last Week", None))
        self.cboPeriod.setItemText(9, QCoreApplication.translate("Stopwatch", u"Last Month", None))
        self.cboPeriod.setItemText(10, QCoreApplication.translate("Stopwatch", u"Daily", None))
        self.cboPeriod.setItemText(11, QCoreApplication.translate("Stopwatch", u"Custom", None))

        self.label_3.setText(QCoreApplication.translate("Stopwatch", u"Currently working on:", None))
        self.btnStart.setText(QCoreApplication.translate("Stopwatch", u"Start", None))
        self.btnAddLap.setText(QCoreApplication.translate("Stopwatch", u"Add Lap", None))
        self.btnDeleteTimer.setText(QCoreApplication.translate("Stopwatch", u"Delete Timer", None))
        self.lblFromFilter.setText(QCoreApplication.translate("Stopwatch", u"From:", None))
        self.label_5.setText(QCoreApplication.translate("Stopwatch", u"To:", None))
        self.btnPencil.setText(QCoreApplication.translate("Stopwatch", u"\u270e", None))
    # retranslateUi

