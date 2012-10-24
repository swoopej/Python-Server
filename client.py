from socket import *

HOST = 'localhost'
PORT = 21555
BUFSIZ = 1024
ADDR = (HOST, PORT)

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(ADDR)

while True:
	data = input('> ')
	if not data:
		break
	clientsock.send(data)
	data = clientsock.recv(BUFSIZ)
	if not data:
		break
	print data

clientsock.close()
