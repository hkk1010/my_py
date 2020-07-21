#! /usr/bin/python
# coding:utf-8


import socket

ip_port=("127.0.0.1",5112)

sk_c=socket.socket()

sk_c.connect(ip_port)

while True:
    inp=input("请输入要发送的信息：").strip()

    if not inp:
        continue
    sk_c.sendall(inp.encode())

    if inp =="exit":
        print("结束通信")
        break
    server_reply=sk_c.recv(1024).decode()
    print(server_reply)