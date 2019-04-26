# Echo client program
import socket
import sys

HOST = 'fd5f:df5:bf3f:0:a75f:3554:2488:6f99'    # The remote host
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
    print(sockaddr)
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client.connect(sockaddr)
    return client

s = CreateClientSocket(HOST, PORT)

with s:
    s.sendall(b'tosend.txt')
    data = s.recv(1024)
    contents = data.decode()
    f = open("received.txt", "w")
    f.write(contents)
print('Received', repr(data))
