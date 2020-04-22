#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
import time
from PYRobot.libs import control

import explorerhat as ep

class explorerhat(control.Control):

    def __init__(self):
        self.mi=0.0
        self.md=0.0
        self.lights={"red":ep.light.red,"green":ep.light.green,"blue":ep.light.blue,"yellow":ep.light.yellow}


    def __Run__(self):
        self.start_worker(self.worker_reader, )
        self.set(0,0)

    def __Close__(self):
        self.set(0,0)

    def worker_reader(self):

        while self.worker_run:
            self.analog_raw=[ep.analog.one.read(),ep.analog.two.read(),ep.analog.three.read(),ep.analog.four.read()]
            #print(self.analog_raw)
            self.analog=[round((x*100)/5) for x in self.analog_raw]
            #print(self.analog)
            time.sleep(self._etc["frec"])

    def get(self):
        return mi,md

    def set(self,mi,md):
        self.mi=mi
        self.md=md
        ep.motor.one.speed(mi)
        ep.motor.two.speed(md)
        self.L_info("Motors velocity: {}:{}".format(self.mi,self.md))
        
    def forward(self,vel):
        self.md=vel 
        self.mi=vel 
        self.set(vel,vel)
        
    def backward(self,vel):
        self.md=vel 
        self.mi=vel 
        self.set(-vel,-vel)

    def stop(self):
        self.set(0,0)
        
    def set_light(self,color,status=True):
        if color in self.lights:
            if status:
                self.lights[color].on()
                #print(color,"on")
            else:
                self.lights[color].off()
                #print(color,"off")
        
        
    def set_pin(self,pin,status):
        pass
    def get_pin(self,pin):
        pass