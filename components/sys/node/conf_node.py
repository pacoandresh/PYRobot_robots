#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2020___________________

from PYRobot.libs.interfaces import Service

class node_interface(Service):
    
    def Run_comp(self,component_name):
        pass
    def Stop_comp(self,component_name):
        pass
    def Get_Interfaces(self,interfaces):
        pass
    def Get_config(self,components):
        pass

_INTERFACES="node_interface"
NODE="localhost"
robot="PYRobot"
name="node"      
frec=0.01
public_sync=False
ethernet="enp0s25"
sys=True
port=8060
broadcast_port=9999
MQTT_port=1883
EMIT_port=10000
mode="public"
KEY="user:pass"


