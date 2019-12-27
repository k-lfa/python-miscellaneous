#!/usr/bin/python3
# coding : utf-8

liste = open('liste', 'r').readlines()
dico = open('dico.txt', 'a')
separator = ['-', '*', '_', '.', '+', '=', '§', '!', ' ', '/', '\\', '&', '~']
nbrange = range(200)

#Word-XX-WORD
for word in liste:
	word = word.rstrip('\n')
	for sep in separator:
		for sep2 in separator:
			for number in nbrange:
				for lastword in liste:
					dico.write(word + sep + str(number) + sep2 + lastword)

#WORD-WORD-WORD
for word in liste:
	word = word.rstrip('\n')
	for sep in separator:
		for sep2 in separator:
			for middleword in liste:
				middleword = middleword.rstrip('\n')
				for lastword in liste:
					dico.write(word + sep + middleword + sep2 + lastword)

#XX-WORD-WORD
for number in range(100):
	for sep in separator:
		for sep2 in separator:
			for middleword in liste:
				word = word.rstrip('\n')
				for finalword in word:
					dico.write(str(number) + sep + middleword + sep2 + finalword )

#WORD-WORD-XX
for word in liste:
	word = word.rstrip('\n')
	for sep in separator:
		for sep2 in separator:
			for middleword in liste:
				middleword = middleword.rstrip('\n')
				for number in nbrange:
					dico.write(word + sep + middleword + sep2 + str(number) + '\n')
