#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________


from PYRobot.libs import utils
from PYRobot.libs.utils_discovery import Discovery
from PYRobot.libs.botlogging.coloramadefs import P_Log
from PYRobot.libs.proxy import Proxy
import PYRobot.libs.parser as parser
import PYRobot.libs.config_comp as conf
import time
import sys
import os.path
import json

robots_dir=utils.get_PYRobots_dir()

sys.path.append(robots_dir)
dir_comp=robots_dir+"components/"

def params(cad):
    if "://" not in cad:
        cad=cad+"://ALL"
    component=parser.get_COMPONENT(cad)
    if component!="":
        model,comp =component.split("://")
        node,comp=comp.split("/")
        return model,node,comp
    else:
        P_Log("{} not valid sintax robot://node/component or robot://component or robot".format(cad))
        exit()

def get_model(cad):
    if os.path.isdir(robots_dir+"/"+cad):
        return cad
    else:
        P_Log("[FR]ERROR {} not is a Model".format(cad))
        exit()
    
def get_robot_json(cad):
    comp="ALL"
    if "://" in cad:
        cad,comp=cad.split("://")

    robot_file=robots_dir+"bin/_Temp/"+cad+".json"
    try:
        with open(robot_file, 'r') as f:
            robot = json.load(f)
        return robot,cad,cad+"/"+comp
    except:
        P_Log("[FR]ERROR loading {} ".format(robot_file))
        raise
        exit()
        
def show_PROC(data,all=True):
    
        P_Log("[FY]COMPONENT:[FW]{} [FY]STATUS:[FG]{}".format(data["_etc"]["name"],data["_PROC"]["status"]))
        P_Log("\t Network:{} Host: {} Pid:{}".
                format(data["_etc"]["ethernet"],data["_etc"]["host"],data["_PROC"]["PID"]))
        if all:
            P_Log("\t[FY] INTERFACES:")
            for t in data["_PROC"]["info"]:
                P_Log("\t\t {} {}".format(t[1],t[0]))
                for w in data["_PROC"]["warnings"][t[0]]:
                    P_Log("\t\t\t Warning: {} not implemented".format(w))
            if len(data["_PROC"]["PUB"])>0:
                P_Log("\t Publicating Topics: {}".format(data["_PROC"]["PUB"]))
            if len(data["_PROC"]["PUB_EVENT"])>0:
                P_Log("\t Publicating Events channels: {}".format(data["_PROC"]["PUB_EVENT"]))
            if len(data["_PROC"]["EMIT"])>0:
                P_Log("\t Emitting Topics: {}".format(data["_PROC"]["EMIT"]))
            if len(data["_PROC"]["EMIT_EVENT"])>0:
                P_Log("\t Emitting Events channels: {}".format(data["_PROC"]["EMIT_EVENT"]))
            if len(data["_PROC"]["SUB"])>0:
                P_Log("\t subscriptions Topics: {}".format(data["_PROC"]["SUB"]))
            if len(data["_PROC"]["SUB_EVENT"])>0:
                P_Log("\t subscribe Events channels: {}".format(data["_PROC"]["SUB_EVENT"]))
            if len(data["_PROC"]["RECEIVE"])>0:
                P_Log("\t Receive Topics: {}".format(data["_PROC"]["RECEIVE"]))
            if len(data["_PROC"]["RECEIVE_EVENT"])>0:
                P_Log("\t Receive Events channels: {}".format(data["_PROC"]["RECEIVE_EVENT"]))
            P_Log("\t Requires: {}".format(data["_PROC"]["requires"]))
            P_Log("")
     


def Start(myrobot):
    robot,robot_name,comp=get_robot_json(myrobot)
    components=robot["COMPONENTS"]
    dsc=Discovery()
    if comp!=robot_name+"/ALL":
        if  comp in components:
            components={comp:components[comp]}
        else:
            P_Log("[FR] {} not found in configuration".format(comp))
            exit()
    for c in components:
        comp=json.dumps(components[c])
        utils.run_component("_comp",comp,run="start")
        i=10
        get=""
        while i>0 and get!=c:
            get=dsc.Get(c+"/Running")
            get=get[0] if len(get)>0 else ""
            i=i-1
            time.sleep(0.1)

    controls=dsc.Get(robot_name+"/*/Control")
    #print(controls)
    for uri in controls.values():
        if uri!="0.0.0.0:0":
                proxy=Proxy(uri)
                if proxy():
                    proxy.Set_Logging(0)
    

if __name__ == '__main__':       
    if len(sys.argv)<2:
        print(len(sys.argv))
        P_Log("please type start/stop/kill/status/create")
        exit()
    if len(sys.argv)>=3:
        if sys.argv[2] in ["kill","stop","status"]:
            robot,node,comp=params(sys.argv[1])

        if sys.argv[2]=="create":
            model=get_model(sys.argv[1])


        if sys.argv[2]=="kill":
            if comp=="ALL":
                pids=utils.findProcessIdByName(robot)
            else:
                pids=utils.findProcessIdByName(robot+"/"+comp)
            for p,n in pids:
                try:
                    utils.kill_process(p)
                    P_Log("[FY]killing [FW]{} PID:{}".format(n,p))
                except:
                    pass
        if sys.argv[2]=="stop":
            if comp =="ALL":
                comp="*"          
            dsc=Discovery()
            controls=dsc.Get(robot+"/"+comp+"/Control")
            #print(controls)
            for uri in controls.values():
                if uri!="0.0.0.0:0":
                    proxy=Proxy(uri)
                    if proxy():
                        proxy.shutdown()
                        
        if sys.argv[2]=="status":
            if comp =="ALL":
                comp="*"          
            dsc=Discovery()
            controls=dsc.Get(robot+"/"+comp+"/Control")
            for uri in controls.values():
                if uri!="0.0.0.0:0":
                    proxy=Proxy(uri)
                    if proxy():
                        info_comp=proxy.Get_INFO()
                        show_PROC(info_comp)
        if sys.argv[2]=="start":
            get_robot_json(sys.argv[1])
            Start(sys.argv[1])

        if sys.argv[2]=="create":
            robot,MODEL=Create_Model(model)
            if len(sys.argv)==4 and sys.argv[3]=="start":
                Start(robot)

