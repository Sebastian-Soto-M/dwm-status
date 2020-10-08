from threading import Thread, Timer

import sh

from dwm_status_events import on_signal, trigger_change_event
from status2d import VerticalBar, xres


class Brightness:
    def __init__(self):
        self.details = ""
        Thread(self.set_details()).start()

    def get_details(self):
        max_b = int(
            str(sh.cat("/sys/class/backlight/intel_backlight/max_brightness")).rstrip())
        actual_b = int(str(
            sh.cat("/sys/class/backlight/intel_backlight/actual_brightness")).rstrip())
        val = int(actual_b*100/max_b)
        bar = VerticalBar(4, val, xres["11"], 5).draw()
        return bar

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(3, self.set_details).start()

    def __str__(self):
        return self.details
