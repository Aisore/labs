#!/bin/python3
import random
import urllib
import re
from bs4 import BeautifulSoup

def num_save(namefile, times, catg, classname):
    with open('namefile', 'a') as my_file:
        infnum = len(open("namefile", 'r').readlines())
        if (times > infnum):
            l = 0
            while l < times:
                number = random.randint(100000,999999)
                m = "https://vk.com/id{}".format(number)
                urllib.request.urlretrieve(url=m, filename='Account.html')
                infile = open('Account.html')
                inffind = infile.find_all('catg', class_="classname")
                for integ in inffind:
                    l += 1
                    my_file.write(int(integ) + "\n")


def mathem_one(filename, fnum):
    infile = open("filename", 'r')
    if (fnum == 0):
        numbers = [float(w) for w in infile.read().split()]
    else:
        numbers = [float(w) for w in infile.readlines(fnum)]
    mean = round(sum(numbers)/len(numbers))
    mens = str(mean)
    