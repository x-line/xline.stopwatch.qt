from datetime import datetime, timedelta

def format_timer_name(timer):

    name = timer.get("name")
    is_running = False
    delta = timedelta()

    for lap in timer.findall("lap"):
        start_txt = lap.get("start") or ''
        end_txt = lap.get("end") or ''

        start = datetime.strptime(start_txt,"%Y-%m-%d %H:%M:%S")
        try:
            end = datetime.strptime(end_txt,"%Y-%m-%d %H:%M:%S")
        except Exception:
            end = datetime.now()     # in future: utcnow()
            is_running = True

        delta += end - start

    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    text = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

    if is_running:
        text = f"* {name} ({text}) Started"
    else:
        text = f"{name} ({text})"

    return text