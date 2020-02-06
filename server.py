#!/usr/bin/python
#coding=utf8

from socketserver import BaseRequestHandler,TCPServer

class EchoHandler(BaseRequestHandler):

    def handle(self):
        print('Got connect from {}'.format(self.client_address))
        data = self.request.recv(8192)
        print('Recv {} from {}'.format(data.decode(),self.client_address))
        self.request.send(data)

if __name__ == '__main__':
    s = TCPServer(('',11111),EchoHandler)
    s.serve_forever()

