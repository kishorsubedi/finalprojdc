#!/usr/bin/env python3



# This code uses Python 2.7. These imports make the 2.7 code feel a lot closer
# to Python 3. (They're also good changes to the language!)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# A few commands are used by both the server and the proxy server. Those
# functions are in library.py.

import socket

# The port that we accept connections on. (A.k.a. "listen" on.)
LISTENING_PORT = 8888

def CreateServerSocket(port):
  """Creates a socket that listens on a specified port.

  Args:
    port: int from 0 to 2^16. Low numbered ports have defined purposes. Almost
        all predefined ports represent insecure protocols that have died out.
  Returns:
    An socket that implements TCP/IP.
  """
  
    #############################################
    #TODO: Implement CreateServerSocket Function
    #############################################
  server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_sock.bind(('localhost', port))
  server_sock.listen()
  return server_sock

def ConnectClientToServer(server_sock):
    # Wait until a client connects and then get a socket that connects to the
    # client.
    
    return server_sock.accept()

    #############################################
    #TODO: Implement CreateClientSocket Function
    #############################################
    


def CreateClientSocket(server_addr, port):
  """Creates a socket that connects to a port on a server."""

    #############################################
    #TODO: Implement CreateClientSocket Function
    #############################################
  

def ReadCommand(sock):
  """Read a single command from a socket. T
  he command must end in newline."""

    #############################################
    #TODO: Implement ReadCommand Function
    #############################################
  data = sock.recv(1024)
  return data.decode()

def ParseCommand(command):
  """Parses a command and returns the command name, first arg, and remainder.

  All commands are of the form:
      COMMAND arg1 remaining text is called remainder
  Spaces separate the sections, but the remainder can contain additional spaces.
  The returned values are strings if the values are present or `None`. Trailing
  whitespace is removed.

  Args:
    command: string command.
  Returns:
    command, arg1, remainder. Each of these can be None.
  """

  args = command.strip().split(' ')
  command = None
  if args:
    command = args[0]
  arg1 = None
  if len(args) > 1:
    arg1 = args[1]
  remainder = None
  if len(args) > 2:
    remainder = ' '.join(args[2:])
  return command, arg1, remainder



def SendText(sock, text):
  """Sends the result over the socket along with a newline."""
  sock.send(text.encode() + b"\n")


def main():
  # Store all key/value pairs in here.
  # The server socket that will listen on the specified port. If you don't
  # have permission to listen on the port, try a higher numbered port.
  server_sock = CreateServerSocket(LISTENING_PORT)

  # Handle commands indefinitely. Use ^C to exit the program.
  while True:
    # Wait until a client connects and then get a socket that connects to the
    # client.
    client_sock, (address, port) = ConnectClientToServer(server_sock)
    print('Received connection from %s:%d' % (address, port))

    # Read a command.
    command_line = ReadCommand(client_sock)
    command, name, text = ParseCommand(command_line)

    # Execute the command based on the first word in the command line.
    
    result = "Hi! I heard you. " + command
    SendText(client_sock, result)

    # We're done with the client, so clean up the socket.

    #################################
    #TODO: Close socket's connection
    #################################
    client_sock.close()



main()
