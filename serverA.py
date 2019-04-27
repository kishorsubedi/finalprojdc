
# Echo server program
from threading import Thread
import os
import socket
import sys
import library


#HOST = 'fd5f:df5:bf3f:0:a75f:3554:2488:6f99'     # Symbolic name meaning all available interfaces
#PORT = 8888             # Arbitrary non-privileged port


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

def main(conn, addr):
    s = library.CreateServerSocket(conn, addr)
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


if __name__ == "__main__":
    serverAddr = 'localhost'
    serverPort = 8080
    if len(sys.argv) > 1:
        serverAddr = sys.argv[1]
    if len(sys.argv) > 2:
        serverPort = sys.argv[2]
    main(serverAddr, serverPort)


