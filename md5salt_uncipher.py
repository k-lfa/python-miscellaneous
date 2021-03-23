#!/usr/bin/python3
# coding : utf-8
import hashlib

salt = b"YOURSTRING"
dico = open('/usr/share/wordlists/rockyou.txt', 'rb').read().splitlines()
hashtofind = 'MD5HASHTOFIND'

for word in dico:
	string = salt + word
	md5_hash = hashlib.md5(string).hexdigest()
	if md5_hash == hashtofind:
		print("found pass : ", word)
