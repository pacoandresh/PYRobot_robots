#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________


frec=0.02
public_sync=False
pins=[4,17,18,27,22]
line=[0,0,0,0,0]


_EVENTS_tracker=[
    "Noline::not any(self.line)",
    "Left::line[0]==1 and line[1]==1",
    "Right::line[3]==1 and line[4]==1"
    ]
