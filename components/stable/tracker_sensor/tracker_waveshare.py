#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
import time
from PYRobot.libs import control
from PYRobot.libs.proxy import Proxy
import json
import RPi.GPIO as GPIO
#import RPi.GPIO as rpi_gpio

class tr_waveshare(control.Control):

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.line=[]
        for p in self.pins:
            GPIO.setup(p,GPIO.IN)
            self.line.append(0)

    def __Run__(self):
        self.start_worker(self.worker_reader, )

    def __Close__(self):
        self.worker_run=False

    def worker_reader(self):
        while self.worker_run:
            for i,p in enumerate(self.pins):
                self.line[i]=GPIO.input(p)
            self._PROC["PUB"].Public(True)
            #self.L_info("line {}".format(self.line))
            time.sleep(self._etc["frec"])

    def get_line(self):
        return self.line
