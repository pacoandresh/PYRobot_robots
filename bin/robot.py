#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2020___________________


from argparse import ArgumentParser
from PYRobot.botlogging.coloramadefs import P_Log,C_Err
import PYRobot.run.command_control as run            

parser = ArgumentParser(description='starter robot PYRobot')

parser.add_argument('robot', help="<file init>.json or <robot name>@<host>/<model>/<components,>", type=str)   
parser.add_argument('command', choices=["start","stop","kill","status"]) 
args = parser.parse_args()



if __name__ == '__main__':       
   init=run.get_robot_init(args.robot)
   print(init)
   run.COMMAND[args.command](Filename=None,Init=init,Model={})

   
