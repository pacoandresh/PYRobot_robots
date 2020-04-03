#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________

from PYRobot.libs.interfaces import Service


frec=0.04
public_sync=False
mi=0.0
md=0.0


_REQUIRES_=["gps"]
_EVENTS_basemotion=[
    "Stop::self.mi==0 and self.md==0",
    "Max::self.mi>255 and self.md>255",
    "Running::self.mi!=0 or self.md!=0",
    "Left::self.mi < self.md",
    "Right::self.mi > self.md",
    "Forward::self.mi==self.md and self.md>0",
    "Backward::self.mi==self.md and self.md<0"
    ]
