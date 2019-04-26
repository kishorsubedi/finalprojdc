#!/usr/bin/env python3

import socket

HOST = 'fd8c:624e:ee6f:0:2017:6e93:f788:fc40'  # The server's hostname or IP address
PORT = 8888     # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall("hello".encode())
    data = s.recv(1024)

print('Received', repr(data))