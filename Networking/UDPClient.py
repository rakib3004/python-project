import socket
serverName = 'hostname'
serverPort = 12000
clientSocket = 'Going to University'
#socket(AF_INET, SOCK_DGRAM)
message = input('Input lowecase sentence')
#clientSocket.sendto(message.encode(,(serverName,serverPort)))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()