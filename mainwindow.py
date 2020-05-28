# This Python file uses the following encoding: utf-8
import sys
import json
from PySide2.QtWidgets import QApplication,QMainWindow, QAction, QListWidget, QComboBox, QMessageBox, QInputDialog, QWidget,QVBoxLayout, QMenu,QLabel, QStackedWidget, QPushButton
from PySide2.QtCore import QDir, QFile, QXmlStreamWriter, QThreadPool, QTimer, QDateTime
import xml.etree.ElementTree as ET
from xml.dom import minidom
from ui_newtimer import Ui_Newtimer
import time
import traceback, sys
from datetime import datetime, timedelta
from reusable_functions import format_timer_name

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Stopwatch')
        self.create_menu()

        main_widget = Ui_Newtimer()
        self.setCentralWidget(main_widget)
        self.show()

        self.threadpool = QThreadPool()
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def recurring_timer(self):

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

    def new_app(self):
        (text, bool) = QInputDialog.getText(None, "New Timer", "Please enter the name of the new timer")
        xml_file_name = QDir.currentPath() + "/Timers v.1.xml"
        #QMessageBox.warning(self, "Message", "Cannot find file %s:\n%s." % (text, xml_file_name))

        if bool and text:
            tree = ET.parse(xml_file_name)
            root = tree.getroot()
            data = ET.Element("Timer", {"name": text})
            root.append(data)
            #root.insert(1, data)
            tree.write("Timers v.1.xml")
            self.window().findChild(QListWidget, "listTimers").addItem(text + " (00:00:00)")
            #self.window().findChild()

    def quit(self):
        self.close()


    def create_menu(self):
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)

        fileMenu = mainMenu.addMenu("File")
        exportMenu = mainMenu.addMenu("Export")

        newAction = QAction("New Timer", self)
        #newAction.setShortcut("Ctrl+N")
        newAction.triggered.connect(self.new_app)

        editAction = QAction("Edit Times", self)
        #editAction.setShortcut("Ctrl+E")
        editAction.triggered.connect(self.new_app)

        deleteAction = QAction("Delete", self)
        #deleteAction.setShortcut("Ctrl+D")
        deleteAction.triggered.connect(self.new_app)

        openAction = QAction("Open Containing Folder", self)
        #openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.new_app)

        quitAction = QAction("Quit", self)
        #openAction.setShortcut("Ctrl+O")
        quitAction.triggered.connect(self.quit)


        salesAction = QAction("Sales Force", self)
        #salesAction.setShortcut("Ctrl+F")
        salesAction.triggered.connect(self.new_app)

        exprtAction = QAction("Export Period By Day", self)
        #exprtAction.setShortcut("Ctrl+E")
        exprtAction.triggered.connect(self.new_app)


        fileMenu.addAction(newAction)
        fileMenu.addAction(editAction)
        fileMenu.addAction(deleteAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(quitAction)


        exportMenu.addAction(salesAction)
        exportMenu.addAction(exprtAction)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
    sys.exit(0)


