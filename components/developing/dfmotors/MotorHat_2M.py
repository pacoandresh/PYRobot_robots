#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
import time
from PYRobot.libs import control
import time
from Adafruit_MotorHAT import Adafruit_MotorHAT

class MotorHat_2M(control.Control):

    def __init__(self):
        pass

    def __Run__(self):
        self._mh = Adafruit_MotorHAT(self.addr)
        self._mi = self._mh.getMotor(self.mi_id)
        self._md = self._mh.getMotor(self.md_id)
        self._mi.run(Adafruit_MotorHAT.RELEASE)
        self._md.run(Adafruit_MotorHAT.RELEASE)


    def __Close__(self):
        self.set_base(0,0)

    def worker_reader(self):
        while self.worker_run:
            time.sleep(self._etc["frec"])

    def set_base(self,mi,md):
        mi_dir=Adafruit_MotorHAT.FORWARD if mi*self.mi_reverse>0 else Adafruit_MotorHAT.BACKWARD
        md_dir=Adafruit_MotorHAT.FORWARD if md*self.md_reverse>0 else Adafruit_MotorHAT.BACKWARD
        self._mi.run(mi_dir)
        self._md.run(md_dir)
        self.mi=mi
        self.md=md
        mi=-self.mi if self.mi<0 else self.mi
        md=-self.md if self.md<0 else self.md

        self._mi.setSpeed(mi)
        self._md.setSpeed(md)
        self._PROC["PUB"].Public()

    def get_base(self):
        return self.mi,self.md
