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
        arr = sh.nmcli("-c", "no").split('\n')[0].split(':')[1].split(' ')
        if arr[1] != 'disconnected':
            return Status2d.color(xres["14"], " ".join(arr[3:]))
        else:
            return Status2d.color(xres["9"], 'Not Connected')

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.ssid = self.get_details()
        Timer(10, self.set_details).start()

    def __str__(self):
        return self.ssid
