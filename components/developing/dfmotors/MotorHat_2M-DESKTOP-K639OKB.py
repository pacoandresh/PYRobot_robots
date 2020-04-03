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
        self.stop()

    def worker_reader(self):
        while self.worker_run:
            time.sleep(self._etc["frec"])

    def set(self,mi,md):
        if mi==0:
            self._mi.run(Adafruit_MotorHAT.RELEASE)
        if mi>0:
            self._mi.setSpeed((mi*255)//100)
            self._mi.run(Adafruit_MotorHAT.FORWARD)
        if mi<0:
            self._mi.setSpeed((-mi*255)//100)
            self._mi.run(Adafruit_MotorHAT.BACKWARD)
            
        if md==0:
            self._md.run(Adafruit_MotorHAT.RELEASE)
        if md>0:
            self._md.setSpeed((md*255)//100)
            self._md.run(Adafruit_MotorHAT.FORWARD)
        if md<0:
            self._md.setSpeed((-md*255)//100)
            self._md.run(Adafruit_MotorHAT.BACKWARD)
        self.mi=(mi*255)//100
        self.md=(md*255)//100
        self._PROC["PUB"].Public()

    def get(self):
        return self.mi,self.md

    def forward(self,vel):
        self.set(vel,vel)

    def backward(self,vel):
        self.set(-vel,-vel)

    def stop(self):
        self._mi.run(Adafruit_MotorHAT.RELEASE)
        self._md.run(Adafruit_MotorHAT.RELEASE)
