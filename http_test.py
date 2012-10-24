import socket
from time import ctime
import os

class Server:
	#class to make a simple http server
	def __init__(self, port = 21555):
		self.host = ''
		self.port = port
		self.bufsiz = 1024

	def run_server(self, port = 21555):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.bind((self.host, self.port))
		self.s.listen(5)

		for x in range(5):
			pid = os.fork()

			if pid == 0:
				print 'waiting for connection on port %s...' % port
				
				try:
					self.clisock, addr = self.s.accept()
					print 'connected from : ', addr

					while True:
						data = self.clisock.recv(1024)

						if not data:
							self.clisock.close()
							break

						self.clisock.send('You sent the following data: %s' % (data))
				except KeyboardInterrupt:
					sys.exit()

		


new_server = Server()
new_server.run_server()
try:
	os.waitpid(-1, 0)
except KeyboardInterrupt:
	sys.exit()
new_server.s.close()

