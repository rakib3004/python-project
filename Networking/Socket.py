import socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org', 80 ))
commandLine ='GET http://data.pr4e.org/intro-short.txt HTTP1.0\r\n\r\n'.encode()
mySocket.send(commandLine)

while True :
    data = mySocket.recv(512)
    if(len(data)<1):
        break
    else:
        print(data.decode(),end=' ')
mySocket.close()

