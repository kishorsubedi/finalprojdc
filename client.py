# Echo client program
import socket
import sys

HOST = 'fd8c:624e:ee6f:0:2017:6e93:f788:fc40'    # The remote host
PORT = 8888              # The same port as used by the server

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
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client.connect(sockaddr)
    return client

s = CreateClientSocket(HOST, PORT)

with s:
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
