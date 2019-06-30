import socket
import threading
import sys
import pickle

class Cliente():
	"""docstring for Cliente"""
	def __init__(self, host="172.16.32.111", port=4000):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		while True:
			msg = input()
			if msg != 'salir':
				self.send_msg(msg)
			else:
				self.sock.close()
				sys.exit()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(data.decode())
			except:
				pass

	def send_msg(self, msg):
		self.sock.send(msg.encode())




c = Cliente()