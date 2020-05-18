#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________

from PYRobot.libs.interfaces import Service


devname="Logitech Logitech Attack 3"
#devname="Sony PLAYSTATION(R)3 Controller"
device=""
phys=""
BUTTONS=[]

frec=0.1
public_sync=False

_REQUEST_=[]


_EVENTS_joystick={"Stop":"self.ABS_X==self.ABS_Y",
                  "Max_X":"self.ABS_X==255",
                  "Max_Y":"self.ABS_Y==255",
                  "Max_Z":"self.ABS_Z==255",
                  "Min_Z":"self.ABS_Z==0"
                }
