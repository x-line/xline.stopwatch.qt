from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

def format_timer_name(timer: 'Timer', filter='Total'):

    today = datetime.today()
    today = datetime(today.year, today.month, today.day)
    start_filter = datetime.min
    end_filter = datetime.max
    if filter == 'Today':
        start_filter = today
        end_filter = today + timedelta(days=1)
    if filter == 'This Week':
        start_filter = today - timedelta(days=today.weekday())
        # end_filter =
    if filter == 'Last Week':
        start_filter = today - timedelta(days=today.weekday() + 7)
        end_filter = today - timedelta(days=today.weekday())

    is_running = False
    delta = timedelta()

    if filter == 'Last Lap':
        pass
        # lap = timer.findall("lap")

    else:
        for lap in timer.laps:
            start = lap.start
            if lap.stopped:
                end = lap.end
                is_running = False
            else:
                end = datetime.now()     # in future: utcnow()
                is_running = True

            # Note this is simplistic. If there is overlap these need to be sliced.
            if start >= start_filter and end < end_filter:
                delta += end - start

    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    text = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

    if is_running:
        text = f"* {timer.name} ({text}) Started"
    else:
        text = f"{timer.name} ({text})"

    return text

def format_timer_name_from_xml(timer: ET.Element, filter='Total'):

    today = datetime.today()
    today = datetime(today.year, today.month, today.day)
    start_filter = datetime.min
    end_filter = datetime.max
    if filter == 'Today':
        start_filter = today
        end_filter = today + timedelta(days=1)
    if filter == 'This Week':
        start_filter = today - timedelta(days=today.weekday())
        # end_filter =
    if filter == 'Last Week':
        start_filter = today - timedelta(days=today.weekday() + 7)
        end_filter = today - timedelta(days=today.weekday())

    name = timer.get("name")
    is_running = False
    delta = timedelta()

    if filter == 'Last Lap':
        pass
        # lap = timer.findall("lap")

    else:
        for lap in timer.findall("lap"):
            start_txt = lap.get("start") or ''
            end_txt = lap.get("end") or ''

            start = datetime.strptime(start_txt,"%Y-%m-%d %H:%M:%S")
            try:
                end = datetime.strptime(end_txt,"%Y-%m-%d %H:%M:%S")
            except Exception:
                end = datetime.now()     # in future: utcnow()
                is_running = True

            # Note this is simplistic. If there is overlap these need to be sliced.
            if start >= start_filter and end < end_filter:
                delta += end - start

    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    text = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

    if is_running:
        text = f"* {name} ({text}) Started"
    else:
        text = f"{name} ({text})"

    return text
