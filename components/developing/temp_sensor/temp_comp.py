#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
import time
from PYRobot.libs import control
from PYRobot.libs.proxy import Proxy
import json

#import RPi.GPIO as rpi_gpio

class temp_sensor(control.Control):

    def __init__(self):
        pass
        #print(self.__dict__)

    def __Run__(self):
        self.temp=10.0
        self.start_worker(self.worker_reader, )

    def __Close__(self):
        self.worker_run=False

    def worker_reader(self):

        while self.worker_run:
            self.temp=self.temp+0.5
            time.sleep(1)

    def get_temp(self):
        pass

    def get_humidity(self):
        pass
