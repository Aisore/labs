#!/bin/python3
import random
import urllib
import re
from bs4 import BeautifulSoup

def num_save(namefile, times, catg, classname):
    with open(namefile, 'w') as my_file:
        infnum = len(open(namefile, 'r').readlines())
        if (times > infnum):
            l = 0
            while l < times:
                number = random.randint(100000,999999)
                m = "https://vk.com/id{}".format(number)
                #### Сохраняем ВСЮ страничку HTML в отдельный файл account.html
                urllib.request.urlretrieve(url=m, filename='Account.html')
                #### читаем наш Account.html
                infile = open('Account.html').read()
                ####отправляем наш Account.html как строку в парсер
                bs_infile = BeautifulSoup(infile, 'html.parser')
                #### ищем наш класснейм(тоесть pp_info для возраста либо pm_counter для кол-ва друзей)
                inffind = bs_infile.find_all(catg, class_=classname)
                try:
                    ####удаляем с полученной строки все буквы, оставляем только цифры.
                    age = re.sub("\D", "", inffind[0].string)
                    if age.isdigit():
                        l += 1
                        my_file.write(age + "\n")
                except:
                    continue