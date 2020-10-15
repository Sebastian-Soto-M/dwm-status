from threading import Thread, Timer

from dwm_status_events import on_signal, trigger_change_event
from shell_exe import execute
from status2d import Status2d, xres


class Keyboard:
    def __init__(self):
        self.details = ""
        self.icon = Status2d.color(xres["4"], "")
        Thread(self.set_details()).start()

    def get_details(self):
        val = execute([["xkblayout-state", "print", "'%n'"]]).replace('\'', '')
        val = Status2d.color(xres["12"], val)
        return f"{self.icon} {val}"

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(5, self.set_details).start()

    def __str__(self):
        return self.details
