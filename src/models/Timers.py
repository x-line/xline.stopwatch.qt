import xml.etree.ElementTree as ET
from os import path
from datetime import datetime, timedelta
from typing import Optional, List
from xml.dom import minidom
from models.Timer import Timer
from models.TimerGroup import TimerGroup
from errors.DuplicateTimerName import DuplicateTimerException

class Timers:

    def __init__(self, timer_file):
        self.timers: List[Timer] = []
        self.groups: List[TimerGroup] = []
        if timer_file:
            self.timer_file = timer_file
            self.reload()

    def exists(self, name):
        exists1 = any((t for t in self.timers if t.name == name))
        exists2 = any((g.exists(name) for g in self.groups))
        return exists1 or exists2

    def create(self, name: str):
        if self.exists(name):
            raise DuplicateTimerException()
        timer = Timer(name)
        self.timers.append(timer)
        # self.save()
        return timer

    def get(self, name: str):
        timer = next((t for t in self.timers if t.name == name), None)
        return timer

    def get_or_create(self, name: str):
        timer = self.get(name)
        if not timer:
            timer = self.create(name)
        return timer

    def delete(self, name: str):
        timer = self.get(name)
        self.timers.remove(timer)
        self.save()

    def reload(self):
        if path.exists(self.timer_file):
            tree = ET.parse(self.timer_file)
            # root = tree.getroot()
            # for timer in root.iter('Timer'):

            self.timers: List[Timer] = []
            for xml in tree.findall("./Timer"):
                self.timers.append(Timer.parse(xml))

            self.groups: List[TimerGroup] = []
            for xml in tree.findall("./Groups"):
                self.groups.append(TimerGroup.parse(xml))

    def save(self):
        xml = self.as_xml_element
        Timers.write(xml, self.timer_file)


    @staticmethod
    def write(xml: ET.Element, timer_file):
        xmlstr = ET.tostring(xml)
        xmlstr = minidom.parseString(xmlstr).toprettyxml(indent="  ")
        with open(timer_file, "w") as f:
            f.write(xmlstr)


    @property
    def as_xml_element(self):
        xml = ET.Element("Timers")
        for timer in self.timers:
            xml.append(timer.as_xml_element)
        for group in self.groups:
            xml.append(group.xml_element)

        return xml
