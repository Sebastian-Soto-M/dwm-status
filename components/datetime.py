#!/bin/python

from dwm_status_events import trigger_change_event
from datetime import datetime
from threading import Timer, Thread


class DateTime:
    def __init__(self):
        self.details = '0000-00-00- 00:00'
        Thread(self.set_details()).start()

    def get_details(self):
        return datetime.now().strftime('%Y-%m-%d - %H:%M:%S')

    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(10, self.set_details).start()

    def __str__(self):
        return self.details
