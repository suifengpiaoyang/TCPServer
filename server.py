#!/usr/bin/python
#coding=utf8

import socket

def echo_handler(address,client_sock):
    print('Got connection from {}'.format(address))
    while True:
        msg = client_sock.recv(8192).strip()
        client_sock.sendall(msg)
    client_sock.close()

def echo_server(address,backlog=5):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock,client_addr = sock.accept()
        echo_handler(client_addr,client_sock)

if __name__ == '__main__':
    echo_server(('',11111))
