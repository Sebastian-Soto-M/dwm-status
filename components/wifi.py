from dwm_status_events import trigger_change_event, on_signal
from shell_exe import execute
from threading import Thread
from subprocess import CalledProcessError
from status2d import Status2d, xres


class Wifi:
    def __init__(self):
        self.ssid = '🖧 '
        Thread(self.set_details()).start()

    def get_details(self):
        try:
            wifi = execute([
                ["nmcli", "-t", "-f", "active,ssid", "d", "wifi"]
            ]).split(':')[1].split('\n')[0]
            return Status2d.color(xres["14"], wifi)
        except CalledProcessError:
            return Status2d.color(xres["9"], 'Not Connected')

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.ssid = self.get_details()

    def __str__(self):
        return self.ssid
