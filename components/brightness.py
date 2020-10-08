from subprocess import Popen, PIPE
from dwm_status_events import trigger_change_event, on_signal
from shell_exe import execute
from threading import Timer, Thread
from status2d import VerticalBar, xres


class Brightness:
    def __init__(self):
        self.details = ""
        Thread(self.set_details()).start()

    def get_details(self):
        light = int(float(execute([["xbacklight", "-get"]])))
        bar = VerticalBar(4, light, xres["11"], 10).draw()
        return bar

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()

    def __str__(self):
        return self.details
