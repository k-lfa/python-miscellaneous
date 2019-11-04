#!/usr/bin/python2.7

import socket, string, time, thread, base64, zlib

host = "irc.dev.ctf"
port = 6667
canal = "challenge"
username = "dave_null"

def main():
	global sock
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((host, port))
	thread.start_new_thread(Listener(),("Thread No:1",2))

def send_data(command):
	sock.send(command + "\n")

def Listener():
	send_data('USER '+ username + " " + username + " " + username + " " + username)
	send_data('NICK '+ username)
	send_data('JOIN '+ canal)
	send_data('PRIVMSG candy :!ep4')
	while True:
		buf = sock.recv(4096)
		msg = string.split(buf)
		print(buf+ "\n")
		print("Communication in progress")
		time.sleep(1)
		if msg[0] == "PING":
			print("You have been pinged")
			sock.send('PONG %s' % msg[1] + '\n')
		elif buf.find(":Candy!Candy@root-me.org PRIVMSG klfa :") == -1:
			time.sleep(2)
			print("Pas de reponse du bot, renvoi de la demande")
			send_data('PRIVMSG candy :!ep4')
			buf = sock.recv(4096)
			print(buf)
		else:
			print("Reception de la chaine ! \nDebut des calculs")
			buf = buf.replace(':Candy!Candy@root-me.org PRIVMSG klfa :', '')
			chaine = string.split(buf)
			chaine = chaine[-1]
			print "chaine to decode : ", chaine
			key = zlib.decompress(base64.b64decode(chaine))
                        print "key is : ", key
			flag = 'PRIVMSG candy !ep4 -rep '+ key
			print(flag)
			send_data(flag)
			buf = sock.recv(4096)
			print(buf)
			print("Fin du game")
			exit
main()
