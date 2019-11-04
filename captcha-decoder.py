#!/usr/bin/python3
import requests, pytesseract, base64, time
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance, ImageFilter

file = open("img.png", "wb")
url = "http://ctf.dev/captcha"
start_time = time.time()

'''
Get captcha
'''
s = requests.session()
r = s.get(url)
interval = time.time() - start_time
print("web query done in ", interval)
soup = BeautifulSoup(r.text, "html.parser")

img = soup.find_all('img')
img = str(img)
img = img.replace('<img src="data:image/png;base64,','')
img = img.replace('"/>',"")

data = base64.b64decode(img)
file.write(data)
file.close()

#############
# Captcha Break
#############

start_time = time.time()
im = Image.open("img.png")
# Filtrage (augmentation du contraste)
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
# Lancement de la procedure de reconnaissance
key = pytesseract.image_to_string(im)
print(key)
interval = time.time() - start_time
print("captcha break in ", interval)

#################
#send key to bot
#################

data = {'cametu': key}
p = s.post(url, data=data)
p = BeautifulSoup(p.text, "html.parser")
flag = p.find_all('p')
print(flag)

