#! /usr/bin/python3
# coding:utf-8

import socket

ip_port=('127.0.0.1',5112)

sk=socket.socket()

sk.bind(ip_port)
sk.listen(5)

print("启动sokcet服务，等待客户端连接。。。。。。。。。")

conn,address=sk.accept()
while True:
    client_data=conn.recv(1024).decode()
    if client_data=="exit":
        exit("通信结束")

    print("来自%s发来的数据：%s" % (address,client_data))

    conn.sendall("服务器已经收到你发的信息".encode())

conn.close()


