#!/bin/python3
import random
import urllib
import re
from bs4 import BeautifulSoup

number = random.randint(100000,999999)
m = "https://vk.com/id{}".format(number)
soup = BeautifulSoup(urllib.request.urlopen(m), 'lxml')
for img in soup.find_all('img'):
	if img.get('alt'):
		print(img.get('alt'))
		if ".jpg" in (img.get('src')):
			print(img.get('src'))
		else:
			print('Too stubborn to show a photo')
		break
	else:
		print("Doesn`t exist.")
		break
print(number)
urllib.request.urlretrieve(url=m, filename='Account.html')
infile = open('Account.html')
lines = infile.readlines()
for i in range(len(lines)):
	line = lines[i]
	if 'div class="pp_last_activity"' in line:
		time = lines[i]
		if 'Online' in time:
			print('Online')
		else:
			print('Offline')
	if 'div class="pp_status"' in line:
		status = lines[i].strip('<div class="pp_status">').strip('</div>')
		print(status)
	else:
		print('The victim has no status')
		break