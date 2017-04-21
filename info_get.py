#!/bin/python3
import random
import urllib
import re
from bs4 import BeautifulSoup

sur_name_g = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
def num_save(namefile, times, catg, classname, flag1, flag2):
    with open(namefile, 'w') as my_file:
        infnum = len(open(namefile, 'r').readlines())
        if (times > infnum):
            l = 0
            while l < times:
                number = random.randint(100000,999999)
                m = "https://vk.com/id{}".format(number)
                urllib.request.urlretrieve(url=m, filename='Account.html')
                infile = open('Account.html').read()
                bs_infile = BeautifulSoup(infile, 'html.parser')
                find_activ = bs_infile.find_all(catg, class_="pp_last_activity")
                if find_activ != [] and find_activ[0].string is not None:
                    last_status = find_activ[0].string
                else:
                    last_status = ""
                find_surname = bs_infile.find_all("title") 
                surname = find_surname[0].string.split()[-1][-1]
                inffind = bs_infile.find_all(catg, class_=classname)
                if inffind != [] and inffind[0].string is not None:
                    if flag2 and ("была" in last_status or surname in sur_name_g):
                        l = write_in_file(inffind[0].string, my_file, l)
                    elif flag1 and ("был" in last_status or surname not in sur_name_g):
                        l = write_in_file(inffind[0].string, my_file, l)
                    elif (flag1 and flag2) or (flag1 == 0 and flag2 == 0):
                        l = write_in_file(inffind[0].string, my_file, l)
                else:
                    continue

def write_in_file(val, ffname, l1):
    age = re.sub("\D", "", val)
    if age.isdigit() and age != "":
        l1 += 1
        ffname.write(age + "\n")
    return l1
