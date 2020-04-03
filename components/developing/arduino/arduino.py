#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
import time
from PYRobot.libs import control
import json
from serial import Serial


class arduino(control.Control):

    def __init__(self):
        self.base=[0,0]
        self.laser=[0,0,0]
        self.json = ""
        self.pt=[0,0]
        self.ir=[0,0,0,0]
        try:
            self.serial = Serial(self.comPort, self.comPortBaud, timeout=3.0)
            if self.serial.isOpen():
                self.L_info(self.serial.name + ' is open..')
        except Exception:
            self.L_info("error opening usbserial")

        print(self.__dict__)
        self.start_worker(self.worker_reader, )

    def worker_reader(self):
        self.serial.flushInput()
        while self.worker_run:
            try:
                line=self.read_serial()
                print(line)
                for k,v in line.items():
                    if hasattr(self,k):
                        setattr(self,k,v)
            except:
                raise
            self._PROC["PUB"].Pub()
            time.sleep(self._etc["frec"])

    def read_serial(self):
        try:
            line = self.serial.readline().decode("utf-8").lower()
            print(line)
            line = line[line.find("{"):line.find("}") + 1]
            return json.loads(line)
        except:
            raise
            return {}

    def command(self, com="ee"):
        # print(com)
        self.serial.write((com + "\r\n").encode())

    def set_base(self,mi,md):
        com = "base " + str(mi) + "," + str(md)
        self.command(com)

    def get_base(self):
        return self.base

    def set_pantilt(self,angp=45,angt=45):
        #self.pt=[angp,angt]
        print(angp,angt)
        self.command("setpt "+str(angp)+ "," + str(angt))

    def set_tilt(self,angle=45):
        self.command("setpantilt "+str(angle))

    def get_pantilt(self):
        return self.pan,self.tilt
