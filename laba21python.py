#!/bin/python3
import random
import urllib
import re
from bs4 import BeautifulSoup

l = 0
my_file = open("some.txt", 'a')
while l < 3:
    number = random.randint(100000,999999)
    m = "https://vk.com/id{}".format(number)
    urllib.request.urlretrieve(url=m, filename='Account.html')
    infile = open('Account.html')
    lines = infile.readlines()
    for i in range(len(lines)):
        line = lines[i]
        if 'div class="pp_info"' in line:
            age = lines[i]
            integ = ''
            ch = 0           
            for n in age:
                if n.isdigit():
                    integ += n
                else:
                    integ += ' '
            for i in integ.split():
                l += 1
                print(i)
                my_file.write(i + "\n") #print age
my_file.close()

infile = open("some.txt", 'r')
numbers = [float(w) for w in infile.read().split()]
mean = round(sum(numbers)/len(numbers))
mens = str(mean)
my_file2 = open("Age.txt", 'w')
my_file2.write("Средний возраст равен: ")
my_file2.write(mens)