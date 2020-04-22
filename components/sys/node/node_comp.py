#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
import time
from PYRobot.libs import control
#from PYRobot.libs.proxy import Proxy
from pprint import pprint

#import RPi.GPIO as rpi_gpio

class node(control.Control):

    def __init__(self):
        pass

    def __Run__(self):
        
        self.start_worker(self.worker_reader, )
        pprint(self.__dict__)

    def __Close__(self):
        self.worker_run=False

    def worker_reader(self):

        while self.worker_run:
            time.sleep(1)

    def Run_comp(self,component_name):
        pass
    def Stop_comp(self,component_name):
        pass
    def Get_Interfaces(self,interfaces):
        pass
    def Get_config(self,components):
        pass