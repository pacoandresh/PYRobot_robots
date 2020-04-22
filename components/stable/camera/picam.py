#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________
#from libs import utils
import time
from PYRobot.libs import control
from io import BytesIO
import struct
import threading
from PYRobot.libs import control
import PYRobot.utils.utils as utils
from picamera import PiCamera
from components.stable.camera.clientsocket import ClientSocket

class picam(control.Control):
    """Set a connection socket to the camera."""
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (self.width, self.height)
        self.camera.framerate = self.framerate
        self.camera.contrast = 0
        self.camera.brightness = 50
        self.camera.video_stabilization = True
        self.camera.image_effect = 'none'
        self.camera.color_effects = None
        self.camera.rotation = 0
        self.camera.hflip = True if not hasattr(self, 'hflip') else self.hflip
        self.camera.vflip = True if not hasattr(self, 'vflip') else self.vflip
        self.buffer = BytesIO()
        self.clients = list()
        self.ip = self._etc["ip"]

    def __Run__(self):
        self.start_worker(self.worker_read)
        self.start_worker(self.removeClosedConnections)

    def __Close__(self):
        self.worker_run=False

    def worker_read(self):
        """Main worker."""
        while self.worker_run:
            for foo in self.camera.capture_continuous(self.buffer, 'jpeg', use_video_port=True):
                # Si hay clientes a la espera...
                while len(self.clients) is 0:
                    time.sleep(2)
                try:
                    self.acceptConnections()
                    streamPosition = self.buffer.tell()
                    for c in self.clients:
                        if c.closed is False:
                            try:
                                if c.connection is not 0:
                                    c.connection.write(
                                        struct.pack('<L', streamPosition))
                                    c.connection.flush()
                            except Exception as e:
                                closer = threading.Thread(
                                    target=self.setAsClosed, args=(c,))
                                closer.start()
                    self.buffer.seek(0)
                    readBuffer = self.buffer.read()
                    for c in self.clients:
                        if c.closed is False:
                            try:
                                if c.connection is not 0:
                                    c.connection.write(readBuffer)
                            except Exception as e:
                                closer = threading.Thread(
                                    target=self.setAsClosed, args=(c,))
                                closer.start()
                    self.buffer.seek(0)
                    self.buffer.truncate()
                except Exception as e:
                    utils.format_exception(e)

    def image(self):
        """Return IP and PORT to socket connection """
        newClient = ClientSocket(self.socket_port + 1)
        self.clients.append(newClient)
        self.initPort = newClient.port
        self.L_info("New Client {}:{}".format(self.ip,newClient.port))
        while not newClient.waitingForConnection:
            time.sleep(0.3)
        return self.ip, newClient.port

    def acceptConnections(self):
        """Accept connections from clients"""
        # print "Aceptando conexiones desde picamera"
        for c in self.clients:
            c.acceptConnection()

    def setAsClosed(self, client, exception="None"):
        """Set client as closed"""
        # print "Client: ", client.getClient(), "closing."
        self.L_info("Client close")
        client.setClosed()
        try:
            client.connection.write(struct.pack('<L', 0))
            client.connection.close()
            client.serverSocket.close()
        except Exception:
            pass
        if exception is not None:
            utils.format_exception(exception)

    def removeClosedConnections(self, sec=20):
        """Cleaner. Remove clients marked as closed every "sec" seconds."""
        while self.worker_run:
            time.sleep(sec)
            # print "Antes:", self.clients
            self.clients = [c for c in self.clients if not c.closed]
            # print "Despues:", self.clients
