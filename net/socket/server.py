# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
print('Socket server:{0}:{1}'.format(HOST,PORT));
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			if not data: break
			#print('[Client]:',repr(data))
			print('[Client]:',data.decode('utf-8'))
			#conn.sendall(data)
			conn.sendall(input('[Server]:').encode('utf-8'))