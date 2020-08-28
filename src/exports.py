import pyperclip
from models.Timers import Timers

class Exports:

    def exportPeriods(self, timers: Timers, periodFilter: str):
        paste = ""
        for timer in timers.timers:
            paste += f'{timer.name}\t\t\n'
            for lap in timer.laps:
                start = lap.start
                end = lap.end # if timer.end else ''
                paste += f'{start}\t{end}\t{lap.task}\n'

        pyperclip.copy(paste)


    def exportPeriodsByDay(self, timers: Timers, periodFilter: str):
        pyperclip.copy("exportPeriodsByDay")