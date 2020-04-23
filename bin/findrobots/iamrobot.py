#!/usr/bin/env python3
#!/usr/bin/env python3
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
import time
from gevent.server import DatagramServer
import netifaces as ni
import socket
import json

broadcast=":9998"

def get_all_ip_eths():
    address = []
    try:
        for x in ni.interfaces():
            add=ni.ifaddresses(x)
            ips=add.get(ni.AF_INET,[])
            if x!="lo":
                if len(ips)>0:
                    address.append(ips[0]["addr"])
    except Exception:
        print("ERROR: get_all_ip_eths")
        raise
    #print(address)
    return address

def get_host_name():
    return socket.gethostname()

class iamrobot(DatagramServer):

    def handle(self, data, address): # pylint:disable=method-hidden
        key=data.decode()
        if key=="PYRobot/HI::get":
            host=get_host_name()
            payload={}
            payload[host]=get_all_ip_eths()
            payload=json.dumps(payload)
            #print(payload)
            self.socket.sendto(payload.encode(), address)


if __name__ == '__main__':
    iamrobot(broadcast).serve_forever()

