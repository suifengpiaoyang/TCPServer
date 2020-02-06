#!/usr/bin/python
#coding=utf8

from socketserver import StreamRequestHandler,TCPServer

class EchoHandler(StreamRequestHandler):

    def handle(self):
        print('Got connect from {}'.format(self.client_address))
        # self.rfile is a file-like object for reading
        self.data = self.rfile.readline().strip()
        print(self.data.decode())
        self.wfile.write(self.data)
#        for line in self.rfile:
#            print('Recv {} from {}'.format(line.decode(),self.client_address)) 
            # self.wfile is a file-like object for writing
#            self.wfile.write(line)

if __name__ == '__main__':
    s = TCPServer(('',11111),EchoHandler)
    s.serve_forever()

