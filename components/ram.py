from subprocess import Popen, PIPE
from dwm_status_events import trigger_change_event
from threading import Timer, Thread
from status2d import Status2d, xres
import sh


class Ram:
    def __init__(self):
        self.details = ''
        self.icon = Status2d.color(xres["3"], " ")
        Thread(self.set_details()).start()

    def get_details(self):
        ram = "{:.2}".format(int(
            ' '.join(sh.sed(sh.free("--mebi"), "-n",
                            "2{p;q}").split()).split()[2]
        )/1024)
        val = Status2d.color(xres["11"], ram)
        return f"{self.icon} {val}"

    @ trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(3, self.set_details).start()

    def __str__(self):
        return self.details
