from socket import *
from time import ctime

class Server:
	#class to make a simple http server
	def __init__(self, port = 21567):
		self.host = ''
		self.port = port
		self.bufsiz = 1024

	def run_server(self, port = 21567):
		self.socket = socket(AF_INET, SOCK_STREAM)
		self.socket.bind((self.host, self.port))
		self.socket.listen(5)

		while True:
			print 'waiting for connection on port %s...' % port
			self.clisock, addr = self.socket.accept()
			print 'connected from : ', addr
			while True:
				data = self.clisock.recv(1024)
				if not data:
					new_server.socket.close()
					break
				self.clisock.send('You sent the following data: %s' % (data))

		new_server.socket.close()


new_server = Server()
new_server.run_server()
