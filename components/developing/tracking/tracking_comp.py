#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
import time
from PYRobot.libs import control
from PYRobot.libs.proxy import Proxy

import RPi.GPIO as gpio

class digital_read(control.Control):

    def __init__(self):
        gpio.setmode(gpio.BCM)
        for pin in self.pins:
            gpio.setup(pin, gpio.IN)

    def __Run__(self):
        self.start_worker(self.worker_reader, )    

    def worker_reader(self):
        while self.worker_run:
            self.digital=[gpio.input(pin) for pin in self.pins]
            time.sleep(self._etc["frec"])


