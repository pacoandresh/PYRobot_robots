#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________

from PYRobot.libs.interfaces import Service


class gps_drive(Service):

    def set_localization(self,x,y,z):
        pass
    def get_localization(self):
        pass

comPort="/dev/ttyS1"
comPortBaud=115200
frec=0.3
public_sync=True
X=0.0
Y=0.0
Z=0.0
temp=0.0
mi=0
md=0
base_event=[]

_REQUIRES_=[]
_EVENTS_gps=[
    "Ymayor::self.Y>self.X"
]
