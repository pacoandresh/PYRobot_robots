#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
import time
from PYRobot.libs import control
#from PYRobot.libs.proxy import Proxy
from pprint import pprint
from PYRobot.config.cmake_skel import CMake,all_interfaces
from PYRobot.utils.utils import get_PYRobots_dir,get_host_name
from PYRobot.utils import utils
from pprint import pprint
hostname=get_host_name()

class node(control.Control):

    def __init__(self):
        pass

    def __Run__(self):    
        pprint(self._PROC)
        print("---")
        pprint(self._etc)
        self.ALL_I=all_interfaces()
        
    def __Close__(self):
        self.worker_run=False


    def Run_comp(self,comp):
        
        utils.run_component("_comp",comp,run="start")
    
    def Get_Interfaces(self,interfaces):
        INTERFACES={}
        errors=[]
        INTERFACES[hostname]=self.ALL_I.get_interfaces(interfaces)
        INTERFACES[hostname]=list(set(INTERFACES[hostname]))
        errors.extend(self.ALL_I.get_error_interfaces(interfaces))
        #print(errors)
        return INTERFACES,errors
                
                
    def Get_config(self,host,components):
        #self.L_info("components")
        errors=[]
        config_comps={}
        #print(components)
        for comp in components:
            c,cls=comp.split("::")
            g=CMake(c)
            errors.extend(g.get_errors(cls))
            config_comps[host+"@"+c+"::"+cls]=g.get_status(cls)
        #pprint(config_comps)
        #print(errors)
        return config_comps,errors