import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import Optional
from xml.dom import minidom

class Fluent:

	start: datetime = datetime.min
	end: Optional[datetime]
	task: Optional[str]

	def __init__(self, start_: datetime = None, end: datetime = None, task: str = None):
		self.start = start_ if start_ is not None else datetime.now()
		self.end = end
		self.task = task

	def stop(self):
		self.end = datetime.now()

	@property
	def stopped(self) -> bool:
			return self.end is not None

	def getTimeSpan(self) -> timedelta:
		if self.end < self.start: # It has not stopped
			return datetime.now() - self.start
		else:
			return self.end - self.start

	def startAsString(self) -> str:
		# Desired: "yyyy/MM/dd HH:mm:ss"
		return f'{self.start:%Y/%b/%d %H:%M:%S}'

	def endAsString(self) -> str:
		if self.end is None:
			return f'{self.start:%Y/%b/%d %H:%M:%S}'
		else:
			return f'{self.start:%Y/%b/%d %H:%M:%S}'

	def durationInMins(self) -> str:
		# C# version returned "" if start or end is NOne
		# Format as "# ###"
		td = self.getTimeSpan()
		mins = td.total_seconds() / 60
		return f'{mins:,.0f}'.replace(',',' ')

	@staticmethod
	def CreateStart():
		fluent = Fluent()
		fluent.start = datetime.now()
		return fluent

	@property
	def as_xml_element(self):
		# currentDT = datetime.now()
		start = self.start.strftime("%Y-%m-%d %H:%M:%S") # get real date time

		xml = ET.Element("lap", {"start": start})
		if self.end:
			end = self.end.strftime("%Y-%m-%d %H:%M:%S") # get real date time
			xml.set('end', end)
		if self.task:
			xml.set('task', self.task)

		return xml

	@staticmethod
	def parse(xml: ET.Element) -> 'Fluent':
		start_txt = xml.get("start") or ''
		end_txt = xml.get("end") or ''
		task = xml.get("task") or ''

		start = datetime.strptime(start_txt, "%Y-%m-%d %H:%M:%S")
		try:
			end = datetime.strptime(end_txt, "%Y-%m-%d %H:%M:%S")
		except Exception:
			end = None      # isRunning = True

		return Fluent(start, end, task)
