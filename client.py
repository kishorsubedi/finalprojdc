# Echo client program
import socket
import sys
import library

#HOST = 'fd5f:df5:bf3f:0:3fa8:a486:a193:f7e2'    # The remote host
#PORT = 7777              # The same port as used by the server


def CreateClientSocket(server_addr, port):
    sockaddr = library.GetIPv6Addr(server_addr, port)
    print(sockaddr)
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client.connect(sockaddr)
    return client

def main(conn, addr):
    s = CreateClientSocket(conn, addr)

    with s:
        s.sendall(b'resource.txt')
        data = s.recv(1024)
        contents = data.decode()
        
        if(contents == "File Not Found\n"):
            print("Client requested invalid filename")
        
        else:
            with open('received.txt', 'w') as writer:
                writer.write(contents)
                writer.close()
                f = open('received.txt', 'r')
                c = f.read()
                print(c)
                f.close()
 
#print('Received', repr(data))
if __name__ == "__main__":
    serverAddr = 'localhost'
    serverPort = 8080
    if len(sys.argv) > 1:
        serverAddr = sys.argv[1]
    if len(sys.argv) > 2:
        serverPort = sys.argv[2]
    main(serverAddr, serverPort)


