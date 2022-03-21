#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:39:46 2022

@author: omari
"""

import socket
import sys
import json

HOST, PORT = socket.gethostname(), 12397

#m ='{"id": 2, "name": "abc"}'
m = {"id": 2, "name": "abc"} # a real dict.


data = json.dumps(m)

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket()
sock.bind((HOST,PORT))
try:
    # Receive data from the server and shut down
    received = sock.recv(1024)
    received = received.decode("utf-8")

finally:
    sock.close()

print ("Received: {}".format(received))

