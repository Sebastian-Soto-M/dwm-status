from dwm_status_events import trigger_change_event
from datetime import datetime
from threading import Timer, Thread
from status2d import Status2d, xres
import sh


class Uptime:
    def __init__(self):
        self.details = ''
        Thread(self.set_details()).start()

    def get_details(self):
        with open('/proc/uptime', 'r') as f:
            uptime_hours = "{:.3}".format(float(f.readline().split()[0])/3600)
            return Status2d.color(xres["13"], " ")+uptime_hours

    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(60 * 5, self.set_details).start()

    def __str__(self):
        return self.details
