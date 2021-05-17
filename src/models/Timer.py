import xml.etree.ElementTree as ET
import date_utils
from datetime import datetime, timedelta
from models.Fluent import Fluent
from models.Target import Target, TargetPeriod
from reusable_functions import format_timer_name
from typing import List

class Timer:

    def __init__(self, name):
        self.name = name
        self.laps: List[Fluent] = []
        self.rate: float
        self.rateFormat: str
        self.target: float
        self.targetPeriod: TargetPeriod
        self.targetExWeekend: bool
        self.targetFmt: str = ''

    def GetLastFluent(self) -> Fluent:
        return self.laps[-1] if self.laps else None

    def start(self, task: str = None):
        # If it is already started do nothing.
        fluent = self.GetLastFluent()
        if fluent and fluent.stopped == False:
            return

        fluent = Fluent.CreateStart()
        fluent.task = task
        self.laps.append(fluent)

    def stop(self, task: str = None):
        # If no last lap or already stopped do nothing
        fluent = self.GetLastFluent()
        if fluent is None or fluent.stopped:
            return
        fluent.stop()
        fluent.task = task
        return fluent

    def set_period_filter(self, filter: str):
        targetPeriod = self.targetPeriod

        if targetPeriod is None:
            self.targetFmt = " "
        elif targetPeriod == 'Week':
            if filter == 'This Week':
                multiplier = datetime.today().isoweekday() / 5
                self.targetFmt = f" ({datetime.today().isoweekday()} / 5 = {self.target * multiplier}) "
            elif filter == 'Last Week':
                self.targetFmt = f" ({self.target}) "
            elif filter == 'This Month':
                business_days = date_utils.business_days()
                business_days_mtd = date_utils.business_days_mtd()
                target = self.target / 5 * business_days_mtd
                self.targetFmt = f" ({business_days_mtd} / {business_days} days = {target:.1f})"
            else:
                self.targetFmt = " "
        else:
            if filter == 'This Week':
                self.targetFmt = f" (-) "
            else:
                self.targetFmt = " "

    def set_period_filter_(self, filter: str):
        targetPeriod = self.targetPeriod

        # if self.targetPeriod == TargetPeriod.Day.value:
        #     self.targetMultiplier = 1
        # elif self.targetPeriod == TargetPeriod.Week.value:
        #     self.targetMultiplier = datetime.today().isoweekday() / 5
        # # elif self.targetPeriod == TargetPeriod.Week.value:
        # #     self.targetMultiplier = datetime.today().isoweekday() / 7
        # elif self.targetPeriod == TargetPeriod.Month.value:
        #     past = 0
        #     days = 0
        #     today = datetime.today()
        #     d = datetime(today.year, today.month, 1)
        #     while d.month == today.month:
        #         if d.isoweekday() not in (6, 7):
        #             days += 1
        #         if d <= today:
        #             past += 1
        #         d += timedelta(days=1)
        #     self.targetMultiplier = past / days if days != 0 else 1
        # elif self.targetPeriod == TargetPeriod.Year.value:
        #     self.targetMultiplier = datetime.today().month / 12
        # else:
        #     raise RuntimeError(f'Invalid TargetPeriod: {self.targetPeriod}')

        if filter == 'Total':
            self.targetFmt = f" ({self.target} per {self.targetPeriod}) "
        elif filter == 'Today':
            if targetPeriod == TargetPeriod.Day.value:
                multiplier = 1
            elif targetPeriod == TargetPeriod.Week.value:
                multiplier = 0.2
            elif targetPeriod == TargetPeriod.Month.value:
                today = datetime.today()
                workdays = 0
                d = datetime(today.year, today.month, 1)
                while d.month == today.month:
                    if d.isoweekday() not in (6, 7):
                        workdays += 1
                    d += timedelta(days=1)
                multiplier = 1 / workdays
            elif targetPeriod == TargetPeriod.Year.value:
                multiplier = 1 / 48 / 5
            else:
                raise RuntimeError(f'Invalid TargetPeriod: {self.targetPeriod}')

            self.targetFmt = f" ({self.target * multiplier} per {filter}) "


        # elif filter == 'Yesterday':
        #     start_filter = today - timedelta(days=1)
        #     end_filter = today
        # elif filter == 'This Week':
        #     start_filter = today - timedelta(days=today.weekday())
        #     # end_filter = today + timedelta(days=7 - today.weekday())
        #     end_filter = start_filter + timedelta(days=7)
        # elif filter == 'Workweek Average':
        #     # * Calculate the Time Worked this week (which may include a sunday)
        #     # * and divide by the number of days worked (but assume we only start work on a monday
        #     # * This gives the Workweek (i.e. Mon-Fri) average
        #     start_filter = today - timedelta(days=today.weekday())
        #     end_filter = today + timedelta(days=7 - today.weekday())
        #     days_worked = today.weekday() + 1  # Mon = 0, Fri = 4
        # elif filter == 'Last Week':
        #     start_filter = today - timedelta(days=today.weekday() + 7)
        #     end_filter = today - timedelta(days=today.weekday())
        # elif filter == 'This Month':
        #     start_filter = datetime(today.year, today.month, 1)
        #     end_filter = start_filter + relativedelta(months=1)
        # elif filter == 'Monthly Average':
        #     start_filter = datetime(today.year, today.month, 1)
        #     end_filter = today + timedelta(days=1)
        #     daygenerator = (start_filter + timedelta(x + 1) for x in range((end_filter - start_filter).days))
        #     business_days = sum(1 for day in daygenerator if day.weekday() < 5)
        # elif filter == 'Last Month':
        #     end_filter = datetime(today.year, today.month, 1)
        #     start_filter = end_filter - relativedelta(months=1)
        # elif filter == 'Daily':
        #     start_filter = fromFilter
        #     end_filter = start_filter + timedelta(days=1)
        # elif filter == 'Custom':
        #     start_filter = fromFilter
        #     end_filter = toFilter

        # targetMultiplier = self.targetMultiplier
        else:
            self.targetFmt = f" ({self.target * 1} per {self.targetPeriod}) "

    @property
    def stopped(self) -> bool:
        fluent = self.GetLastFluent()
        return fluent.stopped if fluent else True

    def format_str(self, filter='Total', fromFilter: datetime = datetime.today(), toFilter: datetime = datetime.today()):
        return format_timer_name(self, filter, fromFilter, toFilter)

    @staticmethod
    def parse(xml: ET.Element) -> 'Timer':
        name = xml.get("name")
        timer = Timer(name)
        timer.rate = xml.get("rate")
        timer.rateFormat = xml.get("rateFormat")
        timer.target = float(xml.get("target", 0))
        timer.targetPeriod = xml.get("targetPeriod")
        timer.targetExWeekend = bool(xml.get("targetExWeekend"))
        for x in xml.findall("lap"):
            timer.laps.append(Fluent.parse(x))
        return timer

    @property
    def as_xml_element(self):
        xml = ET.Element("Timer")
        xml.set("name", self.name)

        if self.rate:
            xml.set("rate", self.rate)
        if self.rateFormat:
            xml.set("rateFormat", self.rateFormat)
        if self.target:
            xml.set("target", str(self.target))
        if self.targetPeriod:
            xml.set("targetPeriod", self.targetPeriod)
        if self.targetExWeekend:
            xml.set("targetExWeekend", str(self.targetExWeekend))

        for lap in self.laps:
            xml.append(lap.as_xml_element)

        return xml
