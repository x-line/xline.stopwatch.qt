# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_addlap.ui'
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


class Ui_addLap(object):
    def setupUi(self, addLap):
        if not addLap.objectName():
            addLap.setObjectName(u"addLap")
        addLap.resize(470, 350)
        addLap.setMaximumSize(QSize(470, 350))
        self.label_description = QLabel(addLap)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(34, 30, 111, 16))
        self.combo_task_desc = QComboBox(addLap)
        self.combo_task_desc.setObjectName(u"combo_task_desc")
        self.combo_task_desc.setGeometry(QRect(160, 22, 201, 32))
        self.combo_task_desc.setEditable(True)
        self.label_duration = QLabel(addLap)
        self.label_duration.setObjectName(u"label_duration")
        self.label_duration.setGeometry(QRect(30, 62, 121, 16))
        self.edit_duration = QLineEdit(addLap)
        self.edit_duration.setObjectName(u"edit_duration")
        self.edit_duration.setGeometry(QRect(163, 60, 121, 21))
        self.edit_duration.setMaxLength(8)
        self.label_hint = QLabel(addLap)
        self.label_hint.setObjectName(u"label_hint")
        self.label_hint.setGeometry(QRect(166, 90, 101, 16))
        self.radio_enow = QRadioButton(addLap)
        self.radio_enow.setObjectName(u"radio_enow")
        self.radio_enow.setGeometry(QRect(40, 150, 100, 20))
        self.radio_snow = QRadioButton(addLap)
        self.radio_snow.setObjectName(u"radio_snow")
        self.radio_snow.setGeometry(QRect(40, 213, 100, 20))
        self.radio_edate = QRadioButton(addLap)
        self.radio_edate.setObjectName(u"radio_edate")
        self.radio_edate.setGeometry(QRect(40, 179, 100, 20))
        self.radio_sdate = QRadioButton(addLap)
        self.radio_sdate.setObjectName(u"radio_sdate")
        self.radio_sdate.setGeometry(QRect(40, 243, 100, 20))
        self.end_time = QDateTimeEdit(addLap)
        self.end_time.setObjectName(u"end_time")
        self.end_time.setGeometry(QRect(180, 179, 194, 22))
        self.start_time = QDateTimeEdit(addLap)
        self.start_time.setObjectName(u"start_time")
        self.start_time.setGeometry(QRect(180, 243, 194, 22))
        self.btn_record = QPushButton(addLap)
        self.btn_record.setObjectName(u"btn_record")
        self.btn_record.setGeometry(QRect(120, 290, 113, 32))
        self.btn_cancel = QPushButton(addLap)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(261, 290, 113, 32))

        self.retranslateUi(addLap)

        QMetaObject.connectSlotsByName(addLap)
    # setupUi

    def retranslateUi(self, addLap):
        addLap.setWindowTitle(QCoreApplication.translate("addLap", u"Dialog", None))
        self.label_description.setText(QCoreApplication.translate("addLap", u"Task Description : ", None))
        self.label_duration.setText(QCoreApplication.translate("addLap", u"Enter the duration : ", None))
        self.label_hint.setText(QCoreApplication.translate("addLap", u"not understand", None))
        self.radio_enow.setText(QCoreApplication.translate("addLap", u"Ending Now", None))
        self.radio_snow.setText(QCoreApplication.translate("addLap", u"Starting Now", None))
        self.radio_edate.setText(QCoreApplication.translate("addLap", u"Ending", None))
        self.radio_sdate.setText(QCoreApplication.translate("addLap", u"Starting At", None))
        self.btn_record.setText(QCoreApplication.translate("addLap", u"Record", None))
        self.btn_cancel.setText(QCoreApplication.translate("addLap", u"Cancel", None))
    # retranslateUi

