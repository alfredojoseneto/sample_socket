#!/usr/bin/env python3

import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(("localhost", 8000))

while True:
    msg = input("Enter a message: ")
    if not msg:
        msg = input("Enter a message: ")
    socket.send(msg.encode())
