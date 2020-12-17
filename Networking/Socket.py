import socket
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.connect('data.pr4e.org', 80)