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
import smbus
import math
import time


class tr_soundfounder(control.Control):

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.line=[0 for x in range(7)]

    def __Run__(self):
        print(self.line)
        self.start_worker(self.worker_reader, )

    def __Close__(self):
        self.worker_run=False

    def read_raw(self):
        for i in range(0, 7):
            try:
                raw_result = self.bus.read_i2c_block_data(self.i2c_addr, 0, 10)
                Connection_OK = True
                break
            except:
                Connection_OK = False
        if Connection_OK:
            return raw_result
        else:
            print("Error accessing %2X" % self.i2c_addr)
            return False

    def read_raw1(self):
        try:
            line = self.bus.read_i2c_block_data(self.i2c_addr, 0, 10)
            print(line)
        except:
            print("error")

    def worker_reader(self):
        while self.worker_run:
            print(self.read_raw())
            time.sleep(self._etc["frec"])

    def get_line(self):
        return self.line
