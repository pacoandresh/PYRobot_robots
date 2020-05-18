#!/usr/bin/env python3

from PYRobot.utils.utils_discovery import Discovery

def _Get_HI(instances):
    interfaces={}
    for d in instances:
        interfaces.update(d)
    #print("get ",interfaces)
    return interfaces

def get_all_host():
    dst=Discovery()
    key="iamrobot/*/HI"
    response=dst.Get(key)
    return response

if __name__ == "__main__":
    hosts=get_all_host()
    if len(hosts)>0:
        print("Host on line:")
        for host,ips in hosts.items():
                ips=",".join(ips)
                print("\t{}: {}".format(host,ips))

    else:
        print("no host online")
        