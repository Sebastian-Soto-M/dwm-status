from threading import Thread, Timer

import sh

from dwm_status_events import on_signal, trigger_change_event
from status2d import VerticalBar, xres


class Volume:
    def __init__(self):
        self.details = ""
        Thread(self.set_details()).start()

    def get_details(self):
        vol = int(sh.pamixer("--get-volume"))
        bar = VerticalBar(4, vol, xres["14"], 5).draw()
        return bar

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(3, self.set_details).start()

    def __str__(self):
        return self.details
