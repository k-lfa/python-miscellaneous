#!/usr/bin/python2.7
import hashlib, requests, time
from bs4 import BeautifulSoup

s = requests.Session()

host = "http://sample.com"

start = time.time()
r = s.get(host)
end = time.time()

print("Request get in", end - start)

soup = BeautifulSoup(r.content, 'html.parser')
for h in soup.find_all('h3'):
	h = h.string
	print('The string is', h)
	hex = hashlib.md5(h.encode())
	crypt = hex.hexdigest()
	print('The hash is', crypt)
	data = {'hash':crypt}

	start = time.time()
	flag = s.post(host, data=data)
	end = time.time()
	print("Post in", end - start)
	print(flag.text)
