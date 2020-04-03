#!/usr/bin/env python3
# ____________developed by paco andres_29/02/2020___________________

from gevent.server import DatagramServer
from gevent import socket
import inspect
import json
import re

buff_size=4096

class discovery(object):
    def __init__(self,broadcast_port=9999,name="client/PYROBOT"):
        self.name=name
        self.broadcast_port=broadcast_port
        self.dst_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dst_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.dst_client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.dst_client.settimeout(0.2)
        self.dst_server = DatagramServer(('', self.broadcast_port), handle=self._receive)
        self.dst_server.start()
        self.status="OK"
        print(self.__dict__)
    

    def dsc_get(self,key):
        
        robot,comp,query=key.split("/")
        key="{}::{}".format(self.name,key)
        self.dst_client.sendto(key.encode(), ("255.255.255.255", self.broadcast_port))
        instances=[]
        try:
           while True:
               data,address = self.dst_client.recvfrom(buff_size)
               data=data.decode()
               instances.append(data)
        except:
            pass
        print("getting",instances)

    def _receive(self, key, address):
        payload=self.name+" hola"
        self.dst_server.sendto(payload.encode(), address)
        # data sender::robot/component/required
        # key=key.decode()
        # sender,query=key.split("::")
        # if sender==self.name:
        #     return False
        # if self.status!="OK":
        #     return False
        # emitter=self.name
        # robot,comp,query=query.split("/")
        # name=robot+"/"+comp
        # name=name.replace("*",".+")
        # name=name.replace("?",".+")
        # if re.match(name,self.name):
        #     if query in self.sends:
        #         payload=self.sends[query]()
        #         if isinstance(payload,(int,float,string,dict)):
        #             payload=list(payload)
        #         for p in payload:
        #             emit="{}::{}".format(emitter,json.dump(p)).encode()
        #             self.dst_server.sendto(payload, address)



if __name__ == '__main__':
    pass