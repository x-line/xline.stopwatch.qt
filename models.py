from datetime import datetime, timedelta
from typing import Optional

class Fluent:

    dirk = 1
    start: datetime = datetime.min
    end: Optional[datetime]
    task: Optional[str]

    def __init__(self, start_: datetime = None, end: datetime = None, task: str = None):
      self.start = start_ if start_ is not None else datetime.utcnow()
      self.end = end
      self.task = task

    def stop(self):
        self.end = datetime.utcnow();

    def isStopped(self) -> bool:
        return self.end is not None

    def getTimeSpan(self) -> timedelta:
      if self.end < self.start: # It has not stopped
        return datetime.utcnow() - self.start
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
