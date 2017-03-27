#!/bin/python3
import random
import urllib
import re
from bs4 import BeautifulSoup
from tkinter import *

def output(event):
    times = int(ent.get())
    l = 0
    my_file = open("some.txt", 'a')
    while l < times:
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
                    my_file.write(i + "\n")
    my_file.close()

    infile = open("some.txt", 'r')
    numbers = [float(w) for w in infile.read().split()]
    mean = round(sum(numbers)/len(numbers))
    mens = str(mean)
    tex.delete(1.0,END)
    tex.insert(END, mens)

root = Tk()
lab = Label(root, text="Для подсчеста среднего возраста \n введите число", font="Arial 18")
ent = Entry(root,width=2)
but = Button(root, text="Посчитать средний возраст пользователей Vk")
tex = Text(root,width=4,height=2,font="12",wrap=WORD)
ent.grid(row=0,column=0,padx=20)
but.grid(row=0,column=1)
tex.grid(row=0,column=2,padx=20,pady=10)
 
but.bind("<Button-1>",output)
 
root.mainloop() 