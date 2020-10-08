from dwm_status_events import trigger_change_event
from datetime import datetime
from threading import Timer, Thread
from status2d import Status2d, xres


class DateTime:
    def __init__(self):
        self.details = ''
        Thread(self.set_details()).start()

    def get_details(self):
        e1 = Status2d.color(xres["7"], " ")
        date = Status2d.color(xres["12"], "%^b %d")
        e2 = Status2d.color(xres["10"], "ﲊ")
        time = Status2d.color(xres["12"], "%H:%M")
        return datetime.now().strftime(f'{e1} {date} {e2} {time}')

    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(10, self.set_details).start()

    def __str__(self):
        return self.details
