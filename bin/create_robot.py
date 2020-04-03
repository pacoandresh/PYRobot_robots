#!/usr/bin/env python3
# ____________developed by paco andres_10/04/2019___________________
import sys
import os
import time
import json
from PYRobot.libs.create_comp import Comp_Create
from PYRobot.libs.utils import get_PYRobots_dir,run_component
import PYRobot.libs.config_comp as conf
from PYRobot.libs.botlogging.coloramadefs import P_Log
import PYRobot.libs.parser as parser
robots_dir=get_PYRobots_dir()
sys.path.append(robots_dir)
dir_comp="components/"

def Get_Init(model):
    dir_etc=robots_dir+model+"/etc/"
    init=conf.get_conf(dir_etc+"init.json")
    return init

def Get_General(model):
    dir_etc=robots_dir+model+"/etc/"
    general=conf.get_conf(dir_etc+"general.json")
    return general

def Get_Instances(model):
    dir_etc=robots_dir+model+"/etc/"
    instances=conf.get_conf(dir_etc+"instances.json")
    return instances


def Create_Model(model):
    Init=Get_Init(model)
    General=Get_General(model)
    Instances=Get_Instances(model)
    Instances={c:data for c,data in Instances.items() if c in Init}
    conf.init_ethernet()
    P_Log(" ")
    MODEL={}
    MODEL["COMPONENTS"]={}
    for comp,config in Instances.items():
        P_Log("[FY]Checking componenet:[FW]{}".format(comp))
        st=Comp_Create(model,General,comp,config)
        component=st.Get_Component()
        MODEL["COMPONENTS"][component["_etc"]["name"]]=component
        P_Log(" ")
        robot=st.robot
    P_Log("[FY]Creating file model:[FW]{}".format(robots_dir+"bin/_Temp/"+robot+".json"))
    with open(robots_dir+"bin/_Temp/"+robot+".json", 'w') as json_file:
        json.dump(MODEL, json_file, indent=4)
    return robot,MODEL
            


if __name__ == '__main__':
    if len(sys.argv)< 2:
        P_Log("please type create_model model")
        exit()
    if len(sys.argv)==2:
        robot,MODEL=Create_Model(sys.argv[1])


        
        
     
        