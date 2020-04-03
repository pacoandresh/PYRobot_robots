#!/usr/bin/env python3
from gevent import socket
from gevent import Timeout
import time
import json

def Get_Host(port=9999,key="hi PYROBOT"):
    host = '255.255.255.255'
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.sendto(key.encode(), (host, port))
    instances=[]
    client.settimeout(1)
    try:
        while True:
            data, address = client.recvfrom(8192)
            instances.append(data.decode())
    except:
        pass
    finally:
        client.close()
    return instances

if __name__ == "__main__":
    data=Get_Host()
    if len(data)>0:
        print("Host on line:")
        for d in data:
            d=json.loads(d)
            for k,v in d.items():
                ips=",".join(v)
                print("\t{}: {}".format(k,ips))

    else:
        print("no host online")
        