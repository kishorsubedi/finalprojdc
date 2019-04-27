# Echo server program
import socket
import sys
import library

HOST = 'fd5f:df5:bf3f:0:3fa8:a486:a193:f7e2'     # Symbolic name meaning all available interfaces
PORT = 7777            # Arbitrary non-privileged port

COMMAND_BUFFER_SIZE = 256

s = library.CreateServerSocket(HOST, PORT)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        try:
            f = open(data.decode(), 'r')
            contents = f.read()
            f.close()
            conn.send(contents.encode())

        except FileNotFoundError:
            conn.send("File Not Found\n".encode())
            # Keep preset values
        
       
