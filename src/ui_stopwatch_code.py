import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from models.Timers import Timers, Timer
from PySide2.QtCore import QCoreApplication, QTimer, Qt, QDateTime
from PySide2.QtWidgets import QListWidgetItem, QMessageBox
from PySide2.QtWidgets import QDialog
from reusable_functions import format_timer_name, format_timer_name_from_xml
from ui_stopwatch import Ui_Stopwatch
# from ui_stopwatch_generated import Ui_Stopwatch

# from ui_addlap import Ui_addLap
from ui_addlap_code import Ui_addLap_Code
from ui_editlaps_code import Ui_frmEditLaps_Code

class Ui_Stopwatch_Code(Ui_Stopwatch):

    def __init__(self, timers: Timers, window):
        super().__init__()
        # self.setupUi(window) # Needed for Generated code, otherwise comment out
        self.timers = timers
        self.initialize_code()

    def initialize_code(self):
        self.cboPeriod.currentTextChanged.connect(self.selectPeriod)
        self.cboPeriod.setCurrentIndex(3)   # This Week
        # self.cboPeriod.setCurrentIndex(5)   # This Month
        self.listTimers.currentItemChanged.connect(self.selectTimer)
        self.listTimers.itemClicked.connect(self.selectTimer)
        self.listTimers.itemDoubleClicked.connect(self.startTimer)
        self.btnStart.hide()
        self.btnStart.clicked.connect(self.startTimer)
        self.btnAddLap.hide()
        self.btnAddLap.clicked.connect(self.addLap)
        self.btnDeleteTimer.setEnabled(0)
        self.btnDeleteTimer.clicked.connect(self.deleteTimer)
        self.btnDeleteTimer.setEnabled(False)
        self.btnPencil.clicked.connect(self.btnPencil_Clicked)
        self.btnEditLaps.clicked.connect(self.btnEditLaps_Clicked)

        today = datetime.today()
        yesterday = today - timedelta(days=1)
        self.dtFromFilter.setDateTime(QDateTime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0))
        self.dtToFilter.setDateTime(QDateTime(today.year, today.month, today.day, 0, 0, 0))
        # self.dtFromFilter.show()
        # self.dtToFilter.show()

        # Initialise Timer state:
        periodFilter = self.cboPeriod.currentText();
        for timer in self.timers.timers:
            timer.set_period_filter(periodFilter)

        self.redraw_timers()    # Populate Timers for the first time:

    def getSelectedTimer(self):
        if not self.listTimers.selectedItems(): return None
        cboItem = self.listTimers.currentItem()
        name = cboItem.data(Qt.UserRole)
        timer = self.timers.get(name)
        return timer

    def redraw_timers(self):
        self.listTimers.clear()
        for timer in self.timers.timers:
            cboItem = QListWidgetItem(timer.format_str(), self.listTimers)
            cboItem.setData(Qt.UserRole, timer.name)
        # xml_file_name = "Timers v.1.xmlx"
        # tree = ET.parse(xml_file_name)
        # root = tree.getroot()
        # for timer in root.iter('Timer'):
        #     name = timer.get("name")
        #     text = format_timer_name_from_xml(timer)
        #     cboItem = QListWidgetItem(text, self.listTimers)
        #     cboItem.setData(Qt.UserRole, name)


    def selectTimer(self):
        if not self.listTimers.selectedItems(): return
        self.btnDeleteTimer.setEnabled(True)
        self.btnStart.show()
        self.btnAddLap.show()

        cboItem = self.listTimers.currentItem()
        name = cboItem.data(Qt.UserRole)
        timer = self.timers.get(name)
        if timer:
            if timer.stopped:
                    self.btnStart.setText(QCoreApplication.translate("Newtimer", "Start", None))
            else:
                    self.btnStart.setText(QCoreApplication.translate("Newtimer", "Stop", None))

            tasks = []
            taskText = None
            for lap in timer.laps:
                taskText = lap.task
                if lap.task:
                    tasks.insert(0, lap.task)
            self.cboTasks.clear()
            for t in set(tasks):
                self.cboTasks.addItem(t)
            self.cboTasks.setCurrentText(taskText)

        self.selected_timer = timer


        # xml_file_name = "Timers v.1.xmlx"
        # tree = ET.parse(xml_file_name)
        # root = tree.getroot()

        # selectName = self.listTimers.currentItem().text()
        # self.cboTasks.clear()

        # if selectName.split(" ")[0] != "*":
        #     xname = selectName.split(" ")[0]
        #     self.btnStart.setText(QCoreApplication.translate("Newtimer", "Start", None))
        # else:
        #     xname = selectName.split(" ")[1]
        #     self.btnStart.setText(QCoreApplication.translate("Newtimer", "Stop", None))
        # for timer in root.iter('Timer'):
        #     tname = timer.get("name")
        #     # print(xname)
        #     if xname == tname:
        #         tasks = []
        #         taskText = None
        #         for lap in timer.iter('lap'):
        #             taskText = lap.get('task')
        #             if taskText:
        #                 tasks.append(taskText)

        #         for t in set(tasks):
        #             self.cboTasks.addItem(t)
        #         self.cboTasks.setCurrentText(taskText)

    def selectPeriod(self):
        # if not self.cboPeriod.selectedItems(): return
        # self.recurring_timer(updatedStopped=True)
        periodFilter = self.cboPeriod.currentText();
        showFilter = periodFilter in ['Daily', 'Custom']
        if showFilter:
            self.lblFromFilter.show()
            self.lblToFilter.show()
            self.dtFromFilter.show()
            self.dtToFilter.show()
        else:
            self.lblFromFilter.hide()
            self.lblToFilter.hide()
            self.dtFromFilter.hide()
            self.dtToFilter.hide()

        for timer in self.timers.timers:
            timer.set_period_filter(periodFilter)

    def btnPencil_Clicked(self):
        editable = self.cboTasks.isEditable()
        self.cboTasks.setEditable(not editable)

    def btnEditLaps_Clicked(self):
        timer = self.getSelectedTimer();
        if not timer:
            timer = self.timers.timers[0]
            # timer = Timer('New Timer')
            # QMessageBox.information(self, 'Select Timer', "No timer selected.\nPlease select timer and try again.", QMessageBox.Ok)
            # return

        dialog = QDialog()
        dialog.ui = Ui_frmEditLaps_Code(timer)
        # dialog.ui = Ui_Form()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(Qt.WA_DeleteOnClose)
        dialog.exec_()
        # dialog.show()
        # dialog.open()

        print(f'Saving changes: {dialog.ui.hasChanges}')
        if dialog.ui.hasChanges:
            self.timers.save()

    def startTimer(self):
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

    # def startTimer(self):
    #     xml_file_name = "Timers v.1.xmlx"
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
    #                 tree.write("Timers v.1.xmlx")

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
    #                 tree.write("Timers v.1.xmlx")
    #
    #                 text = format_timer_name_from_xml(timer, periodFilter)
    #                 self.listTimers.currentItem().setText(text)


    def addLap(self):
        # Ui_addLap(self.listTimers.currentItem().text())

        cboItem = self.listTimers.currentItem()
        name = cboItem.data(Qt.UserRole)
        timer = self.timers.get(name)

        txt = self.listTimers.currentItem().text()
        Ui_addLap_Code(txt, timer)
        print('done!')

        #w = Addlap.Addlap(self)
        #if w.exec_() == QDialog.Accepted:
        #   name = w.projectName.text()
        #    self.workList.addItem(name)



    def deleteTimer(self):
        if not self.listTimers.selectedItems(): return

        cboItem = self.listTimers.currentItem()
        name = cboItem.data(Qt.UserRole)
        timer = self.timers.get(name)
        if timer:
            buttonReply = QMessageBox.question(self, 'Confirm', "Are you sure wish to delete this timer?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.timers.timers.remove(timer)
                self.timers.save()

                self.listTimers.takeItem(self.listTimers.row(cboItem))
                self.listTimers.setCurrentItem(None)
                self.btnDeleteTimer.setEnabled(False)
                self.btnStart.hide()
                self.btnAddLap.hide()

        # tree = ET.parse("Timers v.1.xmlx")
        # root = tree.getroot()

        # if self.listTimers.currentItem().text().split(" ")[0] != "*":
        #     selectName = self.listTimers.currentItem().text().split(" ")[0]
        # else:
        #     selectName = self.listTimers.currentItem().text().split(" ")[1]

        # for child in root.findall('Timer'):
        #     strName = child.get('name')
        #     if strName == selectName:
        #         buttonReply = QMessageBox.question(self, 'Confirm', "Are you sure wish to delete this timer?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #         if buttonReply == QMessageBox.Yes:
        #             for item in self.listTimers.selectedItems():
        #                 self.listTimers.takeItem(self.listTimers.row(item))
        #             #print(self.listTimers.currentItem().text())
        #             root.remove(child)
        #             #print(self.listTimers.currentItem().text())
        #             tree.write('Timers v.1.xml')
        #             self.btnDeleteTimer.setEnabled(False)
        #             self.btnStart.hide()
        #             self.btnAddLap.hide()
