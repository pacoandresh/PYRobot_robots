#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
import time
from PYRobot.libs import control
from PYRobot.libs.proxy import Proxy
import board
import busio
import adafruit_vl6180x

class vl6180x(control.Control):

    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_vl6180x.VL6180X(i2c)
        #print(self.__dict__)




    def __Run__(self):
        self.start_worker(self.worker_reader, )

        


    def __Close__(self):
        pass

    def worker_reader(self):

        while self.worker_run:
            self.distance=self.sensor.range
            #print(self.distance)
            time.sleep(0.1)
