#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2020___________________


from argparse import ArgumentParser,RawTextHelpFormatter
from PYRobot.botlogging.coloramadefs import P_Log,C_Err
import PYRobot.run.command_control as run  
from PYRobot.utils.utils import get_PYRobots_dir,get_host_name

hostname=get_host_name()          





Model_node={"GENERAL":{"ethernet":"enp0s25",
                       "sys":True,
                       "port":7060,
                       "broadcast_port":9999,
                       "MQTT_port":1883,
                       "EMIT_port":10000,
                       "mode":"public",
                       "KEY":"user:pass",
                       "frec":0.2
                       },
      "Node_"+hostname:{"_COMP":"sys/node",
                        "_INTERFACES":"node_interface"
                        }
            }

desc='''
This utility allow control node component

examples:
./node status
   show status if local node are running
./node stop
   stop node local
./node  kill
   kill process nome if process is in cpu queu

./node -r <name host> [stop,status]
 stop or show info if node is running in host 

./node find  
find all nodes actived in a segment network
'''

parser = ArgumentParser( add_help=True,formatter_class=RawTextHelpFormatter,description=desc)

#parser.add_argument('robot', type=str)   
parser.add_argument('command', choices=["start","stop","kill","status","find"]) 
parser.add_argument('-r','--remote', type=str, dest='remote')
args = parser.parse_args()

init=run.Init_Skel


if __name__ == '__main__':
   if args.command in["find"]:
         comps=["PYRobot/Node_*"]
         run.COMMAND[args.command](comps)
   if args.command in ["start"]:
         init=run.get_robot_init("PYRobot@Model_node/Node_"+hostname)
         run.COMMAND[args.command](Filename=None,Init=init,Model=Model_node)
   if args.command in ["status","kill","stop"]:
            comps=["PYRobot/Node_"+hostname]
            if args.remote is not None:
                  comps=["PYRobot/Node_"+args.remote]
            run.COMMAND[args.command](comps)

   
