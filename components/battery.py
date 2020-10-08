from dwm_status_events import trigger_change_event
from datetime import datetime
from threading import Timer, Thread
from status2d import VerticalBar, xres
import sh


class Battery:
    def __init__(self):
        self.details = ''
        Thread(self.set_details()).start()

    def get_details(self):
        cap = int(sh.cat("/sys/class/power_supply/BAT0/capacity"))
        ac = int(sh.cat("/sys/class/power_supply/AC0/online"))
        color = xres["2"]
        if ac == 0:
            color = xres["3"]
            if cap < 25:
                color = xres["1"]
                sh.notify-send("-u", "critical", "Battery Low",
                               "Plug your charger")
        return VerticalBar(4, cap, color, 5).draw()

    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(5, self.set_details).start()

    def __str__(self):
        return self.details
