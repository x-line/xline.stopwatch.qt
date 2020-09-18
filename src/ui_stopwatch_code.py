import xml.etree.ElementTree as ET
from models.Timers import Timers
from PySide2.QtCore import QCoreApplication, QTimer, Qt
from PySide2.QtWidgets import QListWidgetItem
from reusable_functions import format_timer_name, format_timer_name_from_xml
from ui_stopwatch import Ui_Stopwatch

class Ui_Stopwatch_Code(Ui_Stopwatch):

    def __init__(self, timers: Timers):
        super().__init__()
        self.timers = timers
        self.initialize_code()

    def initialize_code(self):
        self.listTimers.itemDoubleClicked.connect(self.startTimer)
        self.btnStart.hide()
        self.btnStart.clicked.connect(self.startTimer)
        self.redraw_timers()    # Populate Timers for the first time:

    def redraw_timers(self):
        self.listTimers.clear()
        xml_file_name = "Timers v.1.xml"
        tree = ET.parse(xml_file_name)
        root = tree.getroot()
        for timer in root.iter('Timer'):
            name = timer.get("name")
            text = format_timer_name_from_xml(timer)
            cboItem = QListWidgetItem(text, self.listTimers)
            cboItem.setData(Qt.UserRole, name)

    def startTimer(self):
        print('Double clicked (inside of ui_stopwatch_code.py)!')
        ui = self
        cboItem = ui.listTimers.currentItem()
        name = cboItem.data(Qt.UserRole)
        timer = self.timers.get(name)
        if timer:
            if timer.stopped:
                taskText = ui.cboTasks.currentText()
                timer.start(taskText)
                ui.btnStart.setText(QCoreApplication.translate("Newtimer", "Stop", None))
            else:
                taskText = ui.cboTasks.currentText()
                timer.stop(taskText)
                ui.btnStart.setText(QCoreApplication.translate("Newtimer", "Start", None))
            self.timers.save()

            periodFilter = ui.cboPeriod.currentText();
            text = format_timer_name(timer, periodFilter)
            cboItem.setText(text)