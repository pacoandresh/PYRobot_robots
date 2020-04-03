#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________

from PYRobot.libs.interfaces import Service


    
class inputPins_interface(Service):
    
    def set_pin(self,pin,status):
        pass
    def get_pin(self,pin):
        pass
    
class light_interface(Service):
    
    def set_light(self,color,status):
        pass

frec=0.005
public_sync=True
mi=0.0
md=0.0
analog=[0,0,0,0]
analog_raw=[0,0,0,0]
input=[0,0,0,0]
output=[0,0,0,0]
button=0



_EVENTS_basemotion=[
    "Stop::self.mi==0 and self.md==0",
    "Max::self.mi>255 and self.md>255",
    "Running::self.mi!=0 or self.md!=0",
    "Left::self.mi < self.md",
    "Right::self.mi > self.md",
    "Forward::self.mi==self.md and self.md>0",
    "Backward::self.mi==self.md and self.md<0"
    ]
