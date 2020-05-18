#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
import time
from PYRobot.libs import control
from PYRobot.libs.proxy import Proxy
import random
#import RPi.GPIO as rpi_gpio

class base(control.Control):

    def __init__(self):
        self.butt=[]
        self.jx=0
        self.jy=0
        self.Define_Topics("mi","md")
        self.mi=0.0
        self.md=0.0


    def __Run__(self):
        self.set(0,0)
        self.start_worker(self.worker_reader, )
        

    def __Close__(self):
        self.set(0,0)

    def worker_reader(self):
        while self.worker_run:
            self.L_info("X={},Y={},Z={} ,BUTT={}".format(self.X,self.Y,self.Z,self.BUTTONS))
            time.sleep(0.05)

    def get(self):
        return self.mi,self.md

    def set(self,mi,md):
        self.mi_PUB(mi)
        self.md_PUB(md)
        self.L_info("Base new velocity:{}-{}".format(self.md,self.mi))
    

