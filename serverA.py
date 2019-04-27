
# Echo server program
from threading import Thread
import os
import socket
import sys
import library


HOST = 'fd5f:df5:bf3f:0:a75f:3554:2488:6f99'     # Symbolic name meaning all available interfaces
PORT = 8888             # Arbitrary non-privileged port


COMMAND_BUFFER_SIZE = 256

class ClientThread(Thread):

    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def ServeClient(self):
        with self.conn:
            print('Connected by', self.addr)
            while True:
                data = self.conn.recv(1024)
                if not data: break
                try:
                    f = open(data.decode(), 'r')
                    contents = f.read()
                    f.close()
                    self.conn.send(contents.encode())

                except FileNotFoundError:
                    self.conn.send("File Not Found\n".encode())
                    # Keep preset values`
        
        self.conn.close()


s = library.CreateServerSocket(HOST, PORT)
clientThreads = []

# Handle commands indefinitely (^C to exit)
while True:
    # Wait until a client connects, then get a socket for the  client.
    conn, addr = s.accept()
    
    newClientThread = ClientThread(conn, addr)
    newClientThread.ServeClient()
    clientThreads.append(newClientThread)


for t in clientThreads:
    t.join()

s.close()


