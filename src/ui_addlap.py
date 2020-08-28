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

import xml.etree.ElementTree as ET
import time
from datetime import datetime
from models.Timers import Timers

class Ui_addLap(QDialog):
    select_text = ""
    def __init__(self, txt):
        QDialog.__init__(self)

        self.select_text = txt

        self.setWindowTitle("Add Lap")
        self.resize(470, 350)
        self.setMinimumSize(QSize(470, 350))
        self.setMaximumSize(QSize(470, 350))

        self.label_description = QLabel(self)
        self.label_description.setObjectName("label_description")
        self.label_description.setGeometry(QRect(34, 30, 111, 16))
        self.combo_task_desc = QComboBox(self)
        self.combo_task_desc.setObjectName("combo_task_desc")
        self.combo_task_desc.setGeometry(QRect(160, 22, 201, 32))
        self.combo_task_desc.setEditable(True)
        self.label_duration = QLabel(self)
        self.label_duration.setObjectName("label_duration")
        self.label_duration.setGeometry(QRect(30, 62, 121, 16))
        self.edit_duration = QLineEdit(self)
        self.edit_duration.setObjectName("edit_duration")
        self.edit_duration.setInputMask('00:00:00')
        self.edit_duration.setGeometry(QRect(165, 60, 121, 21))
        self.edit_duration.setMaxLength(8)
        self.label_hint = QLabel(self)
        self.label_hint.setObjectName("label_hint")
        self.label_hint.setGeometry(QRect(166, 90, 101, 16))
        self.radio_enow = QRadioButton(self)
        self.radio_enow.setObjectName("radio_enow")
        self.radio_enow.setChecked(True)
        self.radio_enow.setGeometry(QRect(40, 150, 100, 20))
        self.radio_snow = QRadioButton(self)
        self.radio_snow.setObjectName("radio_snow")
        self.radio_snow.setGeometry(QRect(40, 213, 100, 20))
        self.radio_edate = QRadioButton(self)
        self.radio_edate.setObjectName("radio_edate")
        self.radio_edate.setGeometry(QRect(40, 179, 100, 20))
        self.radio_sdate = QRadioButton(self)
        self.radio_sdate.setObjectName("radio_sdate")
        self.radio_sdate.setGeometry(QRect(40, 243, 100, 20))

        self.end_time = QDateTimeEdit(self)
        self.end_time.setObjectName("end_time")
        self.end_time.setMinimumDate(QDate.currentDate().addDays(-365))
        self.end_time.setMaximumDate(QDate.currentDate().addDays(365))
        self.end_time.setGeometry(QRect(180, 179, 194, 22))

        self.start_time = QDateTimeEdit(self)
        self.start_time.setObjectName("start_time")
        self.start_time.setMinimumDate(QDate.currentDate().addDays(-365))
        self.start_time.setMaximumDate(QDate.currentDate().addDays(365))
        self.start_time.setGeometry(QRect(180, 243, 194, 22))

        self.btn_record = QPushButton(self)
        self.btn_record.setObjectName("btn_record")
        self.btn_record.setGeometry(QRect(120, 290, 113, 32))
        self.btn_record.clicked.connect(self.recordLap)
        self.btn_cancel = QPushButton(self)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.setGeometry(QRect(261, 290, 113, 32))
        self.btn_cancel.clicked.connect(self.cancelLap)

        self.retranslateUi(self)
        self.exec_()

        #self.window().findChild(QListWidget, "listTimers").currentItem().text()


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, addLap):
        addLap.setWindowTitle(QCoreApplication.translate("addLap", "Dialog", None))
        self.label_description.setText(QCoreApplication.translate("addLap", "Task Description : ", None))
        self.label_duration.setText(QCoreApplication.translate("addLap", "Enter the duration : ", None))
        self.label_hint.setText(QCoreApplication.translate("addLap", "", None))
        self.radio_enow.setText(QCoreApplication.translate("addLap", "Ending Now", None))
        self.radio_snow.setText(QCoreApplication.translate("addLap", "Starting Now", None))
        self.radio_edate.setText(QCoreApplication.translate("addLap", "Ending", None))
        self.radio_sdate.setText(QCoreApplication.translate("addLap", "Starting At", None))
        self.btn_record.setText(QCoreApplication.translate("addLap", "Record", None))
        self.btn_cancel.setText(QCoreApplication.translate("addLap", "Cancel", None))
    # retranslateUi



    def recordLap(self):
        duration = self.edit_duration.text()

        xml_file_name = "Timers v.1.xml"
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

        selectName = self.select_text
        if selectName.split(" ")[0] != "*":
            curName = selectName.split(" ")[0]
        else:
            curName = selectName.split(" ")[1]

        currentDT = datetime.now()
        cur_time = currentDT.strftime("%Y-%m-%d %H:%M:%S") #get real date time

#--------------------------------------------------------------------
        #get difference day
        dt1 = currentDT.day.__int__() * 24 * 3600 + currentDT.hour.__int__()*3600 + currentDT.minute.__int__()*60 + currentDT.second.__int__()

        dH = duration.split(":")[0]
        dM = duration.split(":")[1]
        dS = duration.split(":")[2]
        if dH == "":
            ndH = 0
        else:
            ndH = int(dH)

        if dM == "":
            ndM = 0
        else:
            ndM = int(dM)

        if dS == "":
            ndS = 0
        else:
            ndS = int(dS)

        dt2 = ndH*3600 + ndM*60 + ndS

        dt = dt1 - dt2
        dtDay = dt/(3600*24)
        dt = dt - dt/(3600*24)
        dtHour = dt/3600
        dt = dt - dt/3600
        dtMins = dt/60
        dtSec = dt - dt/60
#--------------------------------------------------------------------

        tempDT = datetime.now()

        timestamp = time.mktime(time.strptime(cur_time, '%Y-%m-%d %H:%M:%S'))

        dt = self.start_time.dateTime()
        dt_string = dt.toString(self.start_time.displayFormat())


        print(dt_string)


        for timer in root.iter('Timer'):
            tname = timer.get("name")
            if curName == tname:
                if self.radio_enow.isChecked():
                    if duration == '::':
                        data = ET.Element("lap", {"start": cur_time, "end" : cur_time, "task": self.combo_task_desc.currentText()})
                    else:
                        data = ET.Element("lap", {"start": cur_time, "end" : cur_time, "task": self.combo_task_desc.currentText()})
                elif self.radio_edate.isChecked():
                    dt = self.end_time.dateTime()
                    dt_string = dt.toString(self.end_time.displayFormat())
                    if duration == '::':
                        data = ET.Element("lap", {"start": cur_time, "end" : dt_string, "task": self.combo_task_desc.currentText()})
                    else:
                        data = ET.Element("lap", {"start": cur_time, "end" : dt_string, "task": self.combo_task_desc.currentText()})
                elif self.radio_snow.isChecked():
                    if duration == '::':
                        data = ET.Element("lap", {"start": cur_time, "end" : cur_time, "task": self.combo_task_desc.currentText()})
                    else:
                        data = ET.Element("lap", {"start": cur_time, "end" : cur_time, "task": self.combo_task_desc.currentText()})
                elif self.radio_sdate.isChecked():
                    dt = self.end_time.dateTime()
                    dt_string = dt.toString(self.end_time.displayFormat())
                    if duration == '::':
                        data = ET.Element("lap", {"start": cur_time, "end" : dt_string, "task": self.combo_task_desc.currentText()})
                    else:
                        data = ET.Element("lap", {"start": cur_time, "end" : dt_string, "task": self.combo_task_desc.currentText()})
                data.tail = '\n    '
                timer.append(data)
                tree.write("Timers v.1.xml")
                # Timers.write(root, "Timers v.1.xml")

                self.close()




    def cancelLap(self):
        self.close()

