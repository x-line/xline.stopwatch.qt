import os
import xml.etree.ElementTree as ET
from datetime import datetime
from xml.dom import minidom
# from models import Timers

xml_file_name = "Timers test.xml"

timers = ET.Element("Timers")
tree = ET.ElementTree(timers)

timer1 = ET.Element("Timer")
timer1.set("name", "Timer 1")
timers.append(timer1)

currentDT = datetime.now()
cur_time = currentDT.strftime("%Y-%m-%d %H:%M:%S") #get real date time
timer1.append(ET.Element("lap", {"start": cur_time, "end" : cur_time, "task": "Task description" }))
timer1.append(ET.Element("lap", {"start": cur_time, "end" : cur_time, "task": "Task description" }))

timer2 = ET.Element("Timer")
timer2.set("name", "Timer 2")
timers.append(timer2)

tree = ET.parse(xml_file_name)
timers = tree.getroot()  # = timers

print('Timers:')
# for timer in root.iter('Timer'):
# for timer in tree.findall("./Timer"):
for timer in timers.findall("./Timer"):
    timer_name = timer.get("name")
    print(timer_name)

xmlstr = ET.tostring(timers)
xmlstr = minidom.parseString(xmlstr).toprettyxml(indent="   ")
with open(xml_file_name, "w") as f:
    f.write(xmlstr)