# Echo client program
import library
import socket
import sys

HOST = 'fd5f:df5:bf3f:0:a75f:3554:2488:6f99'    # The remote host
PORT = 8888              # The same port as used by the server


def CreateClientSocket(server_addr, port):
    sockaddr = library.GetIPv6Addr(server_addr, port)
    print(sockaddr)
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client.connect(sockaddr)
    return client

s = CreateClientSocket(HOST, PORT)

with s:
    s.sendall(b'resourceA.txt')
    data = s.recv(1024)
    contents = data.decode()
    
    if(contents == "File Not Found\n"):
        print("Client requested invalid filename")
    
    else:
        with open('receivedB.txt', 'w') as writer:
            writer.write(contents)
            writer.close()
            f = open('receivedB.txt', 'r')
            c = f.read()
            print(c)
            f.close()
    
#print('Received', repr(data))
