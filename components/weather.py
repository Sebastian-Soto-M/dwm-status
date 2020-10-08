from dwm_status_events import trigger_change_event
import requests
from threading import Timer, Thread
import time
from status2d import Status2d, xres


class Weather:
    def __init__(self, location):
        self.url = 'http://wttr.in/{}?format=1'.format(location)
        self.details = 'loading'
        Thread(self.set_details()).start()

    def get_details(self):
        for _x in range(0, 20):
            try:
                info = requests.get(self.url).text.rstrip()
                return Status2d.color(xres["11"], info)
            except:
                return 'Not Found'

    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        return Timer(60 * 60, self.set_details).start()

    def __str__(self):
        return self.details
