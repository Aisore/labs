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
    infnum = len(open("some.txt", 'r').readlines())
    if (times > infnum):
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
                    for n in age:
                        if n.isdigit():
                            if (int(n) < 100):
                                integ += n
                            else:
                                l -=1
                        else:
                            integ += ' '
                    for i in integ.split():
                        if (int(i) < 1000):
                            l += 1
                            my_file.write(i + "\n")
                        else:
                            l -=1
        my_file.close()
        infile = open("some.txt", 'r')
        numbers = [float(w) for w in infile.read().split()]
        mean = round(sum(numbers)/len(numbers))
        mens = str(mean)
    else:
        infile = open("some.txt", 'r')
        coco = [float(w) for w in infile.readlines(times)]
        mean = round(sum(coco)/len(coco))
        mens = str(mean)
    tex.delete(1.0,END)
    tex.insert(END, mens)

def number_of_friends(event):
    friends = int(ent2.get())
    ch = 0
    my_file2 = open("some2.txt", 'a')
    infnum = len(open("some2.txt", 'r').readlines())
    if (friends > infnum):
        while ch < friends:
            number = random.randint(100000,999999)
            m = "https://vk.com/id{}".format(number)
            urllib.request.urlretrieve(url=m, filename='Account.html')
            infile = open('Account.html')
            lines = infile.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if 'em class="pm_counter"' in line:
                    numfr = lines[i]
                    integ = ''
                    for n in numfr:
                        if n.isdigit():
                            if (int(n) < 1000):
                                integ += n
                            else:
                                ch -=1
                        else:
                            integ += ' '
                    for i in integ.split():
                        if (int(i) < 1000):
                            ch += 1
                            my_file2.write(i + "\n")
                        else:
                            ch -=1
        my_file2.close()
        infile = open("some2.txt", 'r')
        numbers = [float(w) for w in infile.read().split()]
        mean = round(sum(numbers)/len(numbers))
        mens = str(mean)
    else:
        infile = open("some2.txt", 'r')
        coco = [float(w) for w in infile.readlines(friends)]
        mean = round(sum(coco)/len(coco))
        mens = str(mean)
    tex2.delete(1.0,END)
    tex2.insert(END, mens)

root = Tk()
root.title("Laboratory work. Python")


label = Label(root, text="Чтобы посчитать средний возраст пользователей VK \n введите кол-во пользователей в окно слева.", font= "Arial 8")
label.place(relx=0.09, rely=0.07)
label2 = Label(root, text="Чтобы узнать среднее кол-во друзей пользователей VK \n введите кол-во пользователей в окно слева", font= "Arial 8")
label2.place(relx=0.09, rely=0.5)

ent = Entry(root,width=2)
ent2 = Entry(root,width=2)
but = Button(root, text="Посчитать")
but2 = Button(root, text="Посчитать")
tex = Text(root,width=4,height=1,font="12")
tex2 = Text(root,width=4,height=1,font="12")

ent.grid(row=0,column=0,padx=20)
ent2.grid(row=1,column=0,padx=20)
but.grid(row=0,column=1,padx=50)
but2.grid(row=1,column=1,padx=50)
tex.grid(row=0,column=2,padx=20,pady=50)
tex2.grid(row=1,column=2,padx=20,pady=50)


 
but.bind("<Button-1>",output)
but2.bind("<Button-1>",number_of_friends)
 
root.mainloop() 