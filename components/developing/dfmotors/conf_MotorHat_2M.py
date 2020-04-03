#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________

frec=0.3
public_sync=False
mi=0.0
md=0.0
_mi=None
_md=None
mi_trim=0
md_trim=0
md_reverse=1
mi_reverse=-1
mi_id=1
md_id=2
addr=0x60


_REQUIRES_=[]
_EVENTS_basemotion=[
    "Stop::self.mi==0 and self.md==0",
    "Max::self.mi>255 and self.md>255",
    "Running::self.mi!=0 or self.md!=0",
    "Left::self.mi < self.md",
    "Right::self.mi > self.md",
    "Forward::self.mi==self.md and self.md>0",
    "Backward::self.mi==self.md and self.md<0"
    ]
