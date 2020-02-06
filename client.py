import socket

address = ('192.168.31.18',11111)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(address)
s.sendall('CangLaoShi\n'.encode())
# the send data must end of '\n',otherwise it will be 
# block all the time.
# the following code has the same result.
# s.sendall(bytes('CangLaoShi' + '\n' ,'utf-8'))
data = str(s.recv(8192),'utf-8')
print('Recv {} from the remote server.'.format(data))
