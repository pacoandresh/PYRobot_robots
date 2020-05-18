#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2020___________________


from argparse import ArgumentParser,RawTextHelpFormatter
from PYRobot.botlogging.coloramadefs import P_Log,C_Err
import PYRobot.run.command_control as run            
desc='''
This utility allow control robot models
usage with start:
examples:
./robot init_file.json start. read file and start components

./robot <rob_name>@<host>/<model><components,> (coma separated) start
   run a robot with name robot_name 
   start coma separated components if they are in model.
   this components will be ran in <host> indicated

./robot <rob_name>@<model><components,> (coma separated) start
   similar but they are running in localhost by default
   
usage with stop kill status:
examples:
./robot mybot status
   show all components status running in robot mybot
./robot mybot/gps stop
   stop component gps running in mybot (regardless of host where it are running)
./robot mybot/cam* kill
   kill all process whose name begins with mybot/cam (* ? are wilcards)
   all combinations are possible.
'''

parser = ArgumentParser( add_help=True,formatter_class=RawTextHelpFormatter,description=desc)

parser.add_argument('robot', type=str)   
parser.add_argument('command', choices=["start","stop","kill","status","find"]) 

args = parser.parse_args()



if __name__ == '__main__':
   if args.command in ["start"]:
      init=run.get_robot_init(args.robot)
      run.COMMAND[args.command](Filename=None,Init=init,Model={})
   if args.command in ["status","kill","stop","find"]:
          comps=run.get_comp(args.robot)
          run.COMMAND[args.command](comps)
          

   
