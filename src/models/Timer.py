import xml.etree.ElementTree as ET
from reusable_functions import format_timer_name
from models.Fluent import Fluent
from typing import List

class Timer:

    def __init__(self, name):
        self.name = name
        self.laps: List[Fluent] = []

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

    @property
    def stopped(self) -> bool:
        fluent = self.GetLastFluent()
        return fluent.stopped if fluent else True

    def format_str(self, filter='Total'):
        return format_timer_name(self, filter)

    @staticmethod
    def parse(xml: ET.Element) -> 'Timer':
        name = xml.get("name")
        timer = Timer(name)
        for x in xml.findall("lap"):
            timer.laps.append(Fluent.parse(x))
        return timer

    @property
    def as_xml_element(self):
        xml = ET.Element("Timer")
        xml.set("name", self.name)

        for lap in self.laps:
            xml.append(lap.as_xml_element)

        return xml
