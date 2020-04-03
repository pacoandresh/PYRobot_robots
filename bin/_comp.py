#!/usr/bin/env python3
# ____________developed by paco andres_10/04/2019___________________
import sys
import os
import time
import json
from PYRobot.libs.starterComp import Comp_Starter
import PYRobot.libs.utils as utils
from PYRobot.libs.botlogging.coloramadefs import P_Log
import PYRobot.libs.parser as parser
from PYRobot.libs.proxy import Proxy
robots_dir=utils.get_PYRobots_dir()
sys.path.append(robots_dir)
dir_comp=robots_dir+"components/"


def get_node(host):
    uri,bb=Get_BigBrother_proxy()
    if bb():
        return bb.Get_Node(host)
    else:
        return "0.0.0.0:0"

if __name__ == '__main__':
    if len(sys.argv)==4:
        component=json.loads(sys.argv[1])
        #P_Log("[FY]Starting component {}...".format(component["_etc"]["name"]))
        st=Comp_Starter(component)
        st.start()
       