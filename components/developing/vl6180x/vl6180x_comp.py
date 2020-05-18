#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
import time
from PYRobot.libs import control
from PYRobot.libs.proxy import Proxy
import adafruit_vl6180x
import board
import busio


class vl6180x(control.Control):
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_vl6180x.VL6180X(i2c)
        self.Define_Topics("distance")

    def __Run__(self):
        self.distance_PUB(1000)
        self.start_worker(self.worker_reader, )   

    def __Close__(self):
        self.L_info("closed")

    def worker_reader(self):

        while self.worker_run:
            self.distance_PUB(self.sensor.range)
            #self.L_info(self.distance)
            time.sleep(0.02)
