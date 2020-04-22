#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2020___________________


from argparse import ArgumentParser
from PYRobot.botlogging.coloramadefs import P_Log,C_Err
import PYRobot.run.command_control as run  
from PYRobot.utils.utils import get_PYRobots_dir,get_host_name

hostname=get_host_name()          

#Init_node={"NAME":"PYRobot","MODEL":"Model_node","localhost":["Node_"+hostname]}
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
parser = ArgumentParser(description='starter Node Component')

parser.add_argument('command', choices=["start","stop","kill","status"]) 
args = parser.parse_args()

init=run.Init_Skel


if __name__ == '__main__':    
   init=run.get_robot_init("PYRobot@Model_node/Node_"+hostname)
   run.COMMAND[args.command](Filename=None,Init=init,Model=Model_node)

   
