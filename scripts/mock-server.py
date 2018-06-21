#!/bin/env python
import socket
import sys
import os

server_address = '/tmp/uds_socket'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
# Binding the socket and managing the incomming connections works the same as with TCP/IP sockets.
print >>sys.stderr, 'starting up on %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        while True:
            data = connection.recv(1024)
            print >>sys.stderr, 'received "%s"' % len(data)
            if not data:
                print >>sys.stderr, 'no more data from', client_address
                break
    finally:
        # Clean up the connection
        connection.close()
