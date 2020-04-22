#!/usr/bin/env python3
# ____________developed by paco andres_15/04/2019___________________

import time
from PYRobot.libs import control
from io import BytesIO
import struct
import threading
from PYRobot.libs import control
import PYRobot.utils.utils as utils
import cv2
from components.stable.camera.clientsocket import ClientSocket

class usbcam(control.Control):
    """Set a connection socket to the camera."""
    def __init__(self):
        # Stream settings
        self.buffer = BytesIO()
        self.clients = list()
        self.ip = self._etc["ip"]

    def __Run__(self):
        try:
            self.camera = cv2.VideoCapture(self.idcam)
            self.camera.set(cv2.CAP_PROP_FPS, self.framerate)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
            self.start_worker(self.worker_read_usb)
            self.start_worker(self.removeClosedConnections)
        except:
            self.L_error("imposible open camera ")

    def __Close__(self):
        self.worker_run=False

    def worker_read_usb(self):
        """Main worker."""
        while self.worker_run:
            try:
                l, img = self.camera.read()
                convert= cv2.imencode('.jpeg', img)[1].tobytes()
                self.buffer.write(convert)
            except:
                pass
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
        self.socket_port = newClient.port
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
