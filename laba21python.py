#!/bin/python3
import random
import urllib
import re
from bs4 import BeautifulSoup
from tkinter import *
from asd import num_save, mathem_one

def output(event):
    times = int(ent.get())
    num_save("some.txt", times, 'div', "pp_info")
    mathem_one("some.txt", times)           
    tex.delete(1.0,END)
    tex.insert(END, mens)

def number_of_friends(event):
    friends = int(ent2.get())
    num_save("some2.txt", friends, 'em', "pm_counter")
    mathem_one("some2.txt", friends)
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