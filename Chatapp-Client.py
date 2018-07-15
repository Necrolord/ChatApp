#!/usr/bin/python
import socket

var1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

var1.connect(("localhost", 3333))

str_recv = var1.recv(1024)

print(str(str_recv))

str_send = "Hello, the world!"

var1.send(bytes(str_send, 'utf-8'))

str_recv = var1.recv(1024)

print(str(str_recv))
var1.close()
