#!/usr/bin/env python3

import socket

# initilize the socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific host and port
socket.bind(("localhost", 8000))

# start to listen
socket.listen()

# stablish accept of the connection
conn, addr = socket.accept()


while True:
    # recieving data from client
    data = conn.recv(1024)
    if not data:
        break
    print("Data from %s: %s" % (addr, data.decode()))


# close socket
socket.close()
