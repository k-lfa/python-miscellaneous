#!/usr/bin/python3
import binascii

string = str("AaAAAaaAAaaAaaAAAaaAAAAaAaaAAaaaAAaAAAAAAAaaaAaAAAaAAAAAAaAAaaAAAaaaAaAaAaaAAAaaAaAaaaaaAaAAAaaAAaaAaAAaAaaAAaAaAaaaAAaAAaAaaaaaAaAAaAAaAaAaAAaaAaAaaaaaAaAAaaAAAaaaAaAaAaaAAAaaAaaAaAAaAaaAAaaAAaaAAaAaAaaaAAaA")
table = {}
for i in string:
	if i not in table:
		oct = bin(ord(i))[2:]
		table[i] = oct
print(table)

if table.get("A") > table.get("a"):
	A = "1"
	a = "0"
else:
	a = "1"
	A = "0"

print("a = ", a)
print("A = ", A)

string = string.replace("A", A)
string = (string.replace("a", a))

print(string)

flag = binascii.a2b_uu(string)
print(flag)
