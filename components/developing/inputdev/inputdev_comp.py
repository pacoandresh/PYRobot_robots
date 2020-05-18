#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
import time
from PYRobot.libs import control
import evdev
from pprint import pprint

def create_map(capabilities):
    codes={}
    for k,v in capabilities.items():
        for b in v:
            #print(k[0],b[0],type(b[0]))
            if k[0]!="EV_ABS":
                if type(b[0])==str:
                    codes["{}/{}".format(k[1],b[1])]="{}/{}".format(k[0],b[0])
                if type(b[0])==list:
                    codes["{}/{}".format(k[1],b[1])]="{}/{}".format(k[0],b[0][0])
            else:
                codes["{}/{}".format(k[1],b[0][1])]="{}/{}".format(k[0],b[0][0])
    return codes

class inputdev(control.Control):
    def __init__(self):
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        self.device=None
        for d in devices:
            if d.name==self.devname:
                self.L_info("{} located and connected".format(d.name))
                self.devpath=d.path
                self.phys=d.phys
                self.map=create_map(d.capabilities(verbose=True))
                self.device=d
                for k,v in self.map.items():
                    if k.find("3/")==0:
                        _,topic=v.split("/")
                        setattr(self,topic,127)
        if self.device is None:
            self.L_error("device {} not located ".format(self.devname))
            
        self.joystick=[]
        self.Define_Topics("ABS_X","ABS_Y","ABS_Z","BUTTONS","joystick")

    def __Run__(self):
        self.start_worker(self.worker_reader, )

    def worker_reader(self):

        for event in self.device.read_loop():
            if event.type not in [0,4]:
                cod="{}/{}".format(event.type,event.code)
                #self.L_info("EVENT: {} value: {}".format(self.map[cod],event.value))
                if event.type==3:
                    _,topic=self.map[cod].split("/")
                    setattr(self,topic,event.value)
                    self.L_info("ejes: X:{} Y:{} Z:{}".format(self.ABS_X,self.ABS_Y,self.ABS_Z))
                    self.ABS_X_PUB()
                    self.ABS_Z_PUB()
                    self.ABS_Y_PUB()
                if event.type==1:
                    if event.value==1:
                        self.BUTTONS.append(self.map[cod].split("/")[1])
                    if event.value==0:
                        self.BUTTONS.remove(self.map[cod].split("/")[1])
                    self.L_info("Buttons: {} ".format(self.BUTTONS))  
                    self.BUTTONS_PUB()
                self.joystick_PUB()

