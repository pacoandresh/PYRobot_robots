#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2020___________________

from PYRobot.libs.interfaces import Service

class Node_Interface(Service):
    
    def Run_comp(self,comp):
        pass
    def Get_Interfaces(self,interfaces):
        pass
    def Get_config(self,host,components):
        pass

_INTERFACES="Node_Interface"
NODE="localhost"
robot="PYRobot"
name="node"      
frec=0.01
public_sync=False
ethernet="enp0s25"
logging_level=50
sys=True
port=8060
broadcast_port=9999
MQTT_port=1883
EMIT_port=10000
mode="public"
KEY="user:pass"
pepe=[]


