# Echo client program
import socket
import sys

HOST = 'fd5f:df5:bf3f:0:3fa8:a486:a193:f7e2'    # The remote host
PORT = 7777              # The same port as used by the server

def GetIPv6Addr(addr, port):
    # Try to detect whether IPv6 is supported at the present system and
    # fetch the IPv6 address.
    if not socket.has_ipv6:
        raise Exception("the local machine has no IPv6 support enabled")

    addrs = socket.getaddrinfo(addr, port, socket.AF_INET6, 0, socket.SOL_TCP)

    if len(addrs) == 0:
        raise Exception("there is no IPv6 address configured for the address")

    return addrs[0][-1]

def CreateClientSocket(server_addr, port):
    sockaddr = GetIPv6Addr(server_addr, port)
    print(sockaddr)
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client.connect(sockaddr)
    return client

s = CreateClientSocket(HOST, PORT)

with s:
    s.sendall(b'resourceB.txt')
    data = s.recv(1024)
    contents = data.decode()
    #print(contents)
    
    with open('receivedA.txt', 'w') as writer:
       writer.write(contents)
       writer.close()
    f = open('receivedA.txt', 'r')
    c = f.read()
    print(c)
    f.close()
#print('Received', repr(data))
