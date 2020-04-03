#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________
from PYRobot.libs.interfaces import Service

#Definition class interface sopported by componentself.
# all methods declared in this classes must be codificated on component class


class base_motion(Service):

    def set_base(self,mi,md):
        pass

    def get_base(self):
        pass

class pantilt_motion(Service):

    def set_pantilt(self,angp=45,angt=45):
        pass

    def get_pantilt(self):
        pass

# Local configuration by default for component. This is overwrite for configuration
# located in robot instances.json for any intance of class componentself.

comPort="/dev/ttyS0"
comPortBaud=115200
frec=0.05
public_sync=False
base=[0,0]
pant=0
tilt=0

# definition for every event channel  sopported by componentself.

_EVENTS_base_motion=[
    "Stop::self.base[0]==0 and self.base[1]==0",
    "Max::self.base[0]>255 and self.base[1]>255",
    "Running::self.base[0]!=0 or self.base[1]!=0",
    "Left::self.base[0] < self.base[1]",
    "Right::self.base[0] > self.base[1]",
    "Forward::self.base[0]==self.base[1] and self.base[0]>0",
    "Backward::self.base[0]==self.base[1] and self.base[0]<0"
    ]

_EVENTS_pantilt_motion=[
    "Pant_Max::self.pant>=90",
    "Pant_Min::self.pant<=0",
    "tilt_Max::self.tilt>=90",
    "tilt_Min::self.tilt<=0"
    ]
