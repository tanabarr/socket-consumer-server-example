#!/bin/env python
# https://www.quora.com/Using-Python-whats-the-best-way-to-get-stock-data
import socket
import sys
import os

def get_stats(ticker, start, end):
    import fix_yahoo_finance as yf
    return str(yf.download(ticker, start, end).abs())

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = '/tmp/uds_socket'
print >>sys.stderr, 'connecting to %s' % server_address
try:
    sock.connect(server_address)
except socket.error, msg:
    print >>sys.stderr, msg
    sys.exit(1)

try:
    data = get_stats('AAPL','2016-01-01','2018-01-01')
    print >>sys.stderr, 'sending "%s"' % len(data)
    sock.sendall(data)
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
