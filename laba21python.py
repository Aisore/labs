#!/bin/python3
import random
import urllib
import re
from bs4 import BeautifulSoup

my_file = open("some.txt", 'w') 
number = random.randint(100000,999999)
m = "https://vk.com/id{}".format(number)

urllib.request.urlretrieve(url=m, filename='Account.html')
infile = open('Account.html')
lines = infile.readlines()
for i in range(len(lines)):
    line = lines[i]
    if 'div class="pp_last_activity"' in line:
        time = lines[i]
        if 'Online' in time:
            #print('Online')
            my_file.write("Online\n")
        else:
            #print('Offline')
            my_file.write("Offline\n")
    if 'div class="pp_info"' in line:
        age = lines[i]
        integ = ''
        for n in age:
            if n.isdigit():
                integ += n
            else:
                integ += ' '
        for i in integ.split():
            print(i)
            print(my_file.write(i))
my_file.close()