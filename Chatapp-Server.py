#!/usr/bin/python
import socket

var1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

var1.bind(('localhost', 3333))

var1.listen(5)
flag = 0
while True:
    connect, addr = var1.accept()
    print("Connection Address:" + str(addr))

    str_return = "test socket server. Waiting for command."
    connect.sendto(bytes(str_return, 'utf-8'), addr)

    str_recv, temp = connect.recvfrom(1024)
    print(str_recv)

    str_return = "I got your command, it is " + str(str_recv)
    connect.sendto(bytes(str_return, 'utf-8'), addr)

    connect.close()
