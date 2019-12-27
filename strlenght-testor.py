#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket, re, time

hote = "46.30.204.44"
port = 4000

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((hote, port))
connected = True
clientsocket.settimeout(2)
nb = 1
nbchars = nb * 'A'

while True:
	try:
			clientsocket.send(nbchars.encode())
			print("Test with", nb, "A")
			nb += 1
			nbchars = nbchars = nb * 'A'
			reponse = clientsocket.recv(4096)

			if re.findall(r'String is too long', reponse.decode()):
				print("Max size chars : \n")
				print(nb -1)
				quit()

	except socket.timeout:
			pass
			connected = False
			clientsocket = socket.socket()
			clientsocket.settimeout(3)
			while not connected:
				try:
					time.sleep(5)
					clientsocket.connect((hote, port))
					connected = True
				except socket.error:
					clientsocket.close()
					quit()
