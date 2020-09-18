# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_stopwatch.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import json
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import xml.etree.ElementTree as ET
from ui_addlap import Ui_addLap
import time
from datetime import datetime
from reusable_functions import format_timer_name, format_timer_name_from_xml
from models.Timers import Timers


class Ui_Stopwatch(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.label = QLabel(self)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 40, 131, 31))
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(22, 87, 91, 16))
        self.cboPeriod = QComboBox(self)
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
        self.cboPeriod.currentTextChanged.connect(self.selectPeriod)

        self.cboPeriod.setObjectName("cboPeriod")
        self.cboPeriod.setGeometry(QRect(17, 100, 221, 32))

        self.listTimers = QListWidget(self)

        self.listTimers.setObjectName("listTimers")
        self.listTimers.setGeometry(QRect(22, 136, 451, 221))
        #self.listTimers.currentItemChanged.connect(self.selectTimer)
        self.listTimers.itemClicked.connect(self.selectTimer)
        # self.listTimers.itemDoubleClicked.connect(self.startTimer2)

        #lw = self.listTimers
        #for x in range(lw.count()-1):
        #    lw.item(x).setText("XXX")
        #    lw.item(x).text()

        self.label_3 = QLabel(self)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(23, 372, 131, 16))

        self.btnStart = QPushButton(self)
        self.btnStart.setObjectName("btnStart")
        # self.btnStart.hide()
        # self.btnStart.clicked.connect(self.startTimer)

        self.btnStart.setGeometry(QRect(19, 400, 110, 32))
        self.btnAddLap = QPushButton(self)
        self.btnAddLap.setObjectName("btnAddLap")
        self.btnAddLap.hide()
        self.btnAddLap.clicked.connect(self.addLap)
        self.btnAddLap.setGeometry(QRect(257, 400, 110, 32))

        self.btnDeleteTimer = QPushButton(self)
        self.btnDeleteTimer.setObjectName("btnDeleteTimer")
        self.btnDeleteTimer.setGeometry(QRect(369, 400, 110, 32))
        self.btnDeleteTimer.setEnabled(0)
        self.btnDeleteTimer.clicked.connect(self.deleteTimer)
        self.btnDeleteTimer.setEnabled(False)

        self.cboTasks = QComboBox(self)
        self.cboTasks.setObjectName("cboTasks")
        self.cboTasks.setGeometry(QRect(157, 365, 290, 32))
        self.cboTasks.setEditable(False)

        self.btnPencil = QPushButton(self)
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
        self.btnPencil.setFlat(False)
        self.btnPencil.clicked.connect(self.btnPencil_Clicked)

        self.dtFromFilter = QDateTimeEdit(self)
        self.dtFromFilter.setObjectName("dtFromFilter")
        self.dtFromFilter.setGeometry(QRect(320, 75, 151, 22))
        self.dtFromFilter.hide()

        self.dtToPicker = QDateTimeEdit(self)
        self.dtToPicker.setObjectName("dtToPicker")
        self.dtToPicker.setGeometry(QRect(320, 100, 151, 22))
        self.dtToPicker.hide()

        self.label_4 = QLabel(self)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(275, 80, 41, 16))
        self.label_4.hide()

        self.label_5 = QLabel(self)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(276, 100, 41, 16))
        self.label_5.hide()

        self.retranslateUi(self)

        # # Populate Timers for the first time:
        # xml_file_name = "Timers v.1.xml"
        # tree = ET.parse(xml_file_name)
        # root = tree.getroot()
        # for timer in root.iter('Timer'):
        #     name = timer.get("name")
        #     text = format_timer_name_from_xml(timer)
        #     cboItem = QListWidgetItem(text, self.listTimers)
        #     cboItem.setData(Qt.UserRole, name)
        #     # self.listTimers.addItem(text)

        QMetaObject.connectSlotsByName(self)


    # setupUi

    def retranslateUi(self, Newtimer):
        Newtimer.setWindowTitle(QCoreApplication.translate("Newtimer", "Form", None))
        self.label.setText(QCoreApplication.translate("Newtimer", "Stopwatch", None))
        self.label_2.setText(QCoreApplication.translate("Newtimer", "Show Timers:", None))
        self.cboPeriod.setItemText(0, QCoreApplication.translate("Newtimer", "Total", None))
        self.cboPeriod.setItemText(1, QCoreApplication.translate("Newtimer", "Last Lap", None))
        self.cboPeriod.setItemText(2, QCoreApplication.translate("Newtimer", "Today", None))
        self.cboPeriod.setItemText(3, QCoreApplication.translate("Newtimer", "This Week", None))
        self.cboPeriod.setItemText(4, QCoreApplication.translate("Newtimer", "Workweek Average", None))
        self.cboPeriod.setItemText(5, QCoreApplication.translate("Newtimer", "This Month", None))
        self.cboPeriod.setItemText(6, QCoreApplication.translate("Newtimer", "Monthly Average", None))
        self.cboPeriod.setItemText(7, QCoreApplication.translate("Newtimer", "Yesterday", None))
        self.cboPeriod.setItemText(8, QCoreApplication.translate("Newtimer", "Last Week", None))
        self.cboPeriod.setItemText(9, QCoreApplication.translate("Newtimer", "Last Month", None))
        self.cboPeriod.setItemText(10, QCoreApplication.translate("Newtimer", "Daily", None))
        self.cboPeriod.setItemText(11, QCoreApplication.translate("Newtimer", "Custom", None))

        self.label_3.setText(QCoreApplication.translate("Newtimer", "Currently working on:", None))
        self.btnStart.setText(QCoreApplication.translate("Newtimer", "Start", None))
        self.btnAddLap.setText(QCoreApplication.translate("Newtimer", "Add Lap", None))
        self.btnDeleteTimer.setText(QCoreApplication.translate("Newtimer", "Delete Timer", None))
        self.label_4.setText(QCoreApplication.translate("Newtimer", "From:", None))
        self.label_5.setText(QCoreApplication.translate("Newtimer", "To:", None))

        self.btnPencil.setText(QCoreApplication.translate("Stopwatch", u"\u270e", None))
    # retranslateUi



    def selectTimer(self):
        if not self.listTimers.selectedItems(): return
        self.btnDeleteTimer.setEnabled(True)
        self.btnStart.show()
        self.btnAddLap.show()

        xml_file_name = "Timers v.1.xml"
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

        selectName = self.listTimers.currentItem().text()
        self.cboTasks.clear()

        if selectName.split(" ")[0] != "*":
            xname = selectName.split(" ")[0]
            self.btnStart.setText(QCoreApplication.translate("Newtimer", "Start", None))
        else:
            xname = selectName.split(" ")[1]
            self.btnStart.setText(QCoreApplication.translate("Newtimer", "Stop", None))
        for timer in root.iter('Timer'):
            tname = timer.get("name")
            # print(xname)
            if xname == tname:
                tasks = []
                taskText = None
                for lap in timer.iter('lap'):
                    taskText = lap.get('task')
                    if taskText:
                        tasks.append(taskText)

                for t in set(tasks):
                    self.cboTasks.addItem(t)
                self.cboTasks.setCurrentText(taskText)

    def selectPeriod(self):
        # if not self.cboPeriod.selectedItems(): return
        periodFilter = self.cboPeriod.currentText();
        # lw = self.window().findChild(QListWidget, "listTimers")
        # for x in range(lw.count()):

        xml_file_name = "Timers v.1.xml"
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

        # for x in self.listTimers.findItems('', Qt.MatchRegExp):
        for i in range(self.listTimers.count()):
            x = self.listTimers.item(i)

            cnamelist = x.text().split(" ")
            if cnamelist[0] == "*":
                cname = cnamelist[1]
            else:
                cname = cnamelist[0]

            # if cnamelist[0] == "*":
            for timer in root.iter('Timer'):
                timer_name = timer.get("name")

                if cname == timer_name:
                    text = format_timer_name_from_xml(timer, periodFilter)
                    x.setText(text)

    def btnPencil_Clicked(self):
        editable = self.cboTasks.isEditable()
        self.cboTasks.setEditable(not editable)

    # def startTimer(self):
    #     xml_file_name = "Timers v.1.xml"
    #     tree = ET.parse(xml_file_name)
    #     root = tree.getroot()

    #     periodFilter = self.cboPeriod.currentText();
    #     selectName = self.listTimers.currentItem().text()
    #     if selectName.split(" ")[0] != "*":

    #         xname = selectName.split(" (")
    #         currentDT = datetime.now()
    #         tt5 = currentDT.strftime("%Y-%m-%d %H:%M:%S")

    #         self.listTimers.currentItem().setText("* " + selectName)
    #         self.btnStart.setText(QCoreApplication.translate("Newtimer", "Stop", None))
    #         for timer in root.iter('Timer'):
    #             tname = timer.get("name")
    #             if xname[0] == tname:
    #                 # ts = time.time()
    #                 data = ET.Element("lap", {"start": tt5})
    #                 data.tail = '\n        '
    #                 timer.append(data)
    #                 tree.write("Timers v.1.xml")
    #                 # Timers.write(root, "Timers v.1.xml")

    #     else:
    #         # Stop timer:
    #         currentDT = datetime.now()
    #         tt5 = currentDT.strftime("%Y-%m-%d %H:%M:%S")
    #         self.btnStart.setText(QCoreApplication.translate("Newtimer", "Start", None))
    #         for timer in root.iter('Timer'):
    #             tname = timer.get("name")
    #             if selectName.split(" ")[1] == tname:
    #                 timer.find('lap[last()]').set("end", tt5)

    #                 taskText = self.cboTasks.currentText()
    #                 timer.find('lap[last()]').set("task", taskText)
    #                 tree.write("Timers v.1.xml")
    #                 # Timers.write(root, "Timers v.1.xml")


    #                 text = format_timer_name_from_xml(timer, periodFilter)
    #                 self.listTimers.currentItem().setText(text)


    def addLap(self):
        Ui_addLap(self.listTimers.currentItem().text())
        #w = Addlap.Addlap(self)
        #if w.exec_() == QDialog.Accepted:
        #   name = w.projectName.text()
        #    self.workList.addItem(name)



    def deleteTimer(self):
        if not self.listTimers.selectedItems(): return
        tree = ET.parse("Timers v.1.xml")
        root = tree.getroot()

        if self.listTimers.currentItem().text().split(" ")[0] != "*":
            selectName = self.listTimers.currentItem().text().split(" ")[0]
        else:
            selectName = self.listTimers.currentItem().text().split(" ")[1]

        for child in root.findall('Timer'):
            strName = child.get('name')
            if strName == selectName:
                buttonReply = QMessageBox.question(self, 'Confirm', "Are you sure wish to delete this timer?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    for item in self.listTimers.selectedItems():
                        self.listTimers.takeItem(self.listTimers.row(item))
                    #print(self.listTimers.currentItem().text())
                    root.remove(child)
                    #print(self.listTimers.currentItem().text())
                    tree.write('Timers v.1.xml')
                    self.btnDeleteTimer.setEnabled(False)
                    self.btnStart.hide()
                    self.btnAddLap.hide()



            #self.listTimers.addItem(child.get('name'))




