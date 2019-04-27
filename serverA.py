# Echo server program
import socket
import sys
import library

HOST = 'fd5f:df5:bf3f:0:a75f:3554:2488:6f99'     # Symbolic name meaning all available interfaces
PORT = 8888             # Arbitrary non-privileged port

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
        
       
