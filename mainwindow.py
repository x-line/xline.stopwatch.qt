# This Python file uses the following encoding: utf-8
import json
import os
import sys
import time
import traceback, sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from models.Timers import Timers
from PySide2.QtWidgets import QApplication,QMainWindow, QAction, QListWidget, QComboBox, QMessageBox, QInputDialog, QWidget,QVBoxLayout, QMenu,QLabel, QStackedWidget, QPushButton
from PySide2.QtCore import QDir, QFile, QXmlStreamWriter, QThreadPool, QTimer, QDateTime
from reusable_functions import format_timer_name
from src.exports import Exports
from ui_stopwatch import Ui_Stopwatch
from xml.dom import minidom

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Stopwatch')
        self.create_menu()

        self.timer_file = "Timers v.1.xml"
        self.create_or_load_timers()

        main_widget = Ui_Stopwatch()
        self.setCentralWidget(main_widget)
        self.show()

        self.threadpool = QThreadPool()
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def create_or_load_timers(self):
        self.timers = Timers(self.timer_file)
        if not os.path.exists(self.timer_file):
            self.timers.save()

    def recurring_timer(self):

        # This file gets parsed several times a second...!
        xml_file_name = "Timers v.1.xml"
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

        cboPeriod = self.window().findChild(QComboBox, "cboPeriod")
        periodFilter = cboPeriod.currentText();

        lw = self.window().findChild(QListWidget, "listTimers")
        for x in range(lw.count()):

            cnamelist= lw.item(x).text().split(" ")
            if cnamelist[0] == "*":
                cname = cnamelist[1]
            else:
                cname = cnamelist[0]

            if cnamelist[0] == "*":
                for timer in root.iter('Timer'):
                    timer_name = timer.get("name")

                    if cname == timer_name:
                        text = format_timer_name(timer, periodFilter)
                        lw.item(x).setText(text)

    def new_timer(self):
        (text, ok) = QInputDialog.getText(None, "New Timer", "Please enter the name of the new timer")
        xml_file_name = QDir.currentPath() + "/Timers v.1.xml"
        # QMessageBox.warning(self, "Message", "Cannot find file %s:\n%s." % (text, xml_file_name))

        if ok and text:
            tree = ET.parse(xml_file_name)
            root = tree.getroot()
            data = ET.Element("Timer", {"name": text})
            root.append(data)
            #root.insert(1, data)
            tree.write("Timers v.1.xml")
            # Timers.write(root, "Timers v.1.xml")

            # Code work in progrss:
            # timers = Timers()
            # timers.append(Timer(text))
            # timers.save()

            # Test load and save...


            self.window().findChild(QListWidget, "listTimers").addItem(text + " (00:00:00)")
            #self.window().findChild()

    def exportPeriods(self):
        cboPeriod = self.window().findChild(QComboBox, "cboPeriod")
        periodFilter = cboPeriod.currentText();
        timers = Timers(self.timer_file)

        exports = Exports()
        exports.exportPeriods(timers, periodFilter)

    def exportPeriodsByDay(self):
        cboPeriod = self.window().findChild(QComboBox, "cboPeriod")
        periodFilter = cboPeriod.currentText();
        timers = Timers(self.timer_file)

        exports = Exports()
        exports.exportPeriodsByDay(timers, periodFilter)

    def quit(self):
        self.close()


    def create_menu(self):
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)

        fileMenu = mainMenu.addMenu("File")
        exportMenu = mainMenu.addMenu("Export")

        newAction = QAction("New Timer", self)
        #newAction.setShortcut("Ctrl+N")
        newAction.triggered.connect(self.new_timer)

        editAction = QAction("Edit Times", self)
        #editAction.setShortcut("Ctrl+E")
        editAction.triggered.connect(self.new_timer)

        deleteAction = QAction("Delete", self)
        #deleteAction.setShortcut("Ctrl+D")
        deleteAction.triggered.connect(self.new_timer)

        openAction = QAction("Open Containing Folder", self)
        #openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.new_timer)

        quitAction = QAction("Quit", self)
        #openAction.setShortcut("Ctrl+O")
        quitAction.triggered.connect(self.quit)

        exportPeriods = QAction("Export Period", self)
        #exportPeriods.setShortcut("Ctrl+F")
        exportPeriods.triggered.connect(self.exportPeriods)

        exprtAction = QAction("Export Period By Day", self)
        #exprtAction.setShortcut("Ctrl+E")
        exprtAction.triggered.connect(self.exportPeriodsByDay)


        fileMenu.addAction(newAction)
        fileMenu.addAction(editAction)
        fileMenu.addAction(deleteAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(quitAction)
        exportMenu.addAction(exportPeriods)
        exportMenu.addAction(exprtAction)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
    sys.exit(0)


