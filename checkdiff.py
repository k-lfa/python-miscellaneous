#!/usr/bin/python2.7

key = open("key", "r").read()
secret = open("secret", "r").read()

Nkey = []
Nsecret = []
flag = []
nb = 0

for c in key:
	Nkey.append(c)

for c in secret:
	Nsecret.append(c)


for i in Nsecret:
	if i in Nkey[nb]:
		nb += 1
	else:
		flag.append(i)

print(''.join(flag))


