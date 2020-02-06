import socket

address = ('192.168.31.18',11111)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(address)
s.send('CangLaoShi'.encode())
data = s.recv(8192).decode()
print('Recv {} from the remote server.'.format(data))
