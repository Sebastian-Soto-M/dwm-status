from dwm_status_events import trigger_change_event, on_signal
import re
import sh
from threading import Timer, Thread
from subprocess import CalledProcessError
from status2d import Status2d, xres


class Wifi:
    def __init__(self):
        self.ssid = ''
        Thread(self.set_details()).start()

    def get_details(self):
        wifi_status = sh.nmcli("-t", "-c", "no", "-f",
                               "active,ssid", "d", "wifi").split('\n')
        wifi = ""
        for current in wifi_status:
            if re.search(r'^yes:', current):
                wifi = current.strip('yes:')
                break
        return Status2d.color(xres["14"], wifi) if wifi != "" else Status2d.color(xres["9"], 'Not Connected')

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.ssid = self.get_details()
        Timer(10, self.set_details).start()

    def __str__(self):
        return self.ssid
