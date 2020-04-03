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
        self.mi=0.0
        self.md=0.0


    def __Run__(self):
        self.basemotion=[]
        self.set(0,0)
        #self.start_worker(self.worker_reader, )

    def __Close__(self):
        self.set(0,0)

    def worker_reader(self):

        while self.worker_run:

            self.mi=self.mi+1
            self.md=self.md+0.5
            if self.mi-self.md==50:
                self.mi,self.md=self.md,self.mi
            time.sleep(0.05)

    def get(self):
        return mi,md

    def set(self,mi,md):
        self.mi=mi
        self.md=md
        self.L_info("Base new velocity:{}-{}".format(self.md,self.mi))
        self._PROC["PUB"].Public()
