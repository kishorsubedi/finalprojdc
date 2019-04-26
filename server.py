# Echo server program
import socket
import sys

HOST = 'fd8c:624e:ee6f:0:2017:6e93:f788:fc40'       # Symbolic name meaning all available interfaces
PORT = 8888             # Arbitrary non-privileged port

COMMAND_BUFFER_SIZE = 256

def GetIPv6Addr(addr, port):
    # Try to detect whether IPv6 is supported at the present system and
    # fetch the IPv6 address.
    if not socket.has_ipv6:
        raise Exception("the local machine has no IPv6 support enabled")

    addrs = socket.getaddrinfo(addr, port, socket.AF_INET6, 0, socket.SOL_TCP)

    if len(addrs) == 0:
        raise Exception("there is no IPv6 address configured for the address")

    return addrs[0][-1]


def CreateServerSocket(addr, port):
    """Creates a socket that listens on a specified port.

    Args:
        addr: ip address or "localhost" which will be used as a listening
                socket for the server.
        port: int from 0 to 2^16. Low numbered ports have defined purposes. Almost
                all predefined ports represent insecure protocols that have died out.
    Returns:
        An socket that implements TCP/IP.
    """
    sockaddr = GetIPv6Addr(addr, port)
    print(sockaddr)

    server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(sockaddr)
    server.listen()
    return server

s = CreateServerSocket(HOST, PORT)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
