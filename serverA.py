'''
# Echo server program
import socket
import sys
import library

HOST = 'fd5f:df5:bf3f:0:a75f:3554:2488:6f99'     # Symbolic name meaning all available interfaces
PORT = 8888             # Arbitrary non-privileged port


COMMAND_BUFFER_SIZE = 256

def ServeClient(conn, addr):
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
        

s = library.CreateServerSocket(HOST, PORT)
conn, addr = s.accept()
ServeClient(conn, addr)
s.close()
'''

import selectors
import socket
import sys
import library

HOST = 'localhost'     # Symbolic name meaning all available interfaces
PORT = 8888             # Arbitrary non-privileged port


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

sel = selectors.DefaultSelector()
# ...
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print('listening on', (HOST, PORT))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)

