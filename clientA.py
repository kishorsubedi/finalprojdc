# Echo client program
import socket
import sys
import library

HOST = 'fd5f:df5:bf3f:0:3fa8:a486:a193:f7e2'    # The remote host
PORT = 7777              # The same port as used by the server


def CreateClientSocket(server_addr, port):
    sockaddr = library.GetIPv6Addr(server_addr, port)
    print(sockaddr)
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client.connect(sockaddr)
    return client

s = CreateClientSocket(HOST, PORT)

with s:
    s.sendall(b'resourceB.txt')
    data = s.recv(1024)
    contents = data.decode()
    
    if(contents == "File Not Found\n"):
        print("Client requested invalid filename")
    
    else:
        with open('receivedA.txt', 'w') as writer:
            writer.write(contents)
            writer.close()
            f = open('receivedA.txt', 'r')
            c = f.read()
            print(c)
            f.close()
 
#print('Received', repr(data))
