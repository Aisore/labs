#!/bin/python3
import random
import urllib
import re
from bs4 import BeautifulSoup
from tkinter import *
from info_get import num_save
from average_value import mathem_one, find_slice

ages_file = "some.txt"
friends_number = "some2.txt"
open(ages_file, 'a').close()
open(friends_number, 'a').close()
text_avg_age = "Чтобы посчитать средний возраст пользователей VK \n введите кол-во пользователей в окно слева."
text_avg_friends = "Чтобы узнать среднее кол-во друзей пользователей VK \n введите кол-во пользователей в окно слева"
 
def output():
    label.config(text = "Wait till I'm done...")
    label.update_idletasks()
    label.config(text=text_avg_age, font= "Arial 8")
    times = int(ent.get())
    infile_a = open(ages_file, 'r').read().split()
    if times <= len(infile_a):
        means = find_slice(infile_a, times)
    else:
        num_save(ages_file, times, 'div', "pp_info", var1.get(), var2.get())
        means = mathem_one(ages_file)
    tex.delete(1.0, END)
    tex.insert(END, means)
    


def number_of_friends():
    label2.config(text = "Wait till I'm done...")
    label2.update_idletasks()
    label2.config(text=text_avg_friends, font= "Arial 8")
    friends = int(ent2.get())
    infile_f = open(friends_number, 'r').read().split()
    if friends <= len(infile_f):
        means = find_slice(infile_f, friends)
    else:
        num_save(friends_number, friends, 'em', "pm_counter", var1.get(), var2.get())
        means = mathem_one(friends_number)
    tex2.delete(1.0, END)
    tex2.insert(END, means)

def quit():
    global root
    root.quit()

root = Tk()
root.title("Laboratory work. Python")


label = Label(root, text=text_avg_age, font= "Arial 8")
label.place(relx=0.09, rely=0.07)
label2 = Label(root, text=text_avg_friends, font= "Arial 8")
label2.place(relx=0.09, rely=0.5)


ent = Entry(root, width=2)
ent2 = Entry(root, width=2)
but = Button(root, text="Посчитать", command=output)
but2 = Button(root, text="Посчитать", command=number_of_friends)
tex = Text(root, width=4, height=1, font="12")
tex2 = Text(root, width=4, height=1, font="12")
exitbt = Button(root, text='Выход', command=quit)


var1 = IntVar()
c1 = Checkbutton(root, text="Мужчины", variable=var1)
var2 = IntVar()
c2 = Checkbutton(root, text="Женщины", variable=var2)


ent.grid(row=0, column=0, padx=20)
c1.place(relx=0.12, rely=0.35)
c2.place(relx=0.5, rely=0.35)
ent2.grid(row=3, column=0, padx=20)
but.grid(row=0, column=1, padx=50)
but2.grid(row=3, column=1, padx=50)
tex.grid(row=0, column=2, padx=20, pady=50)
tex2.grid(row=3, column=2, padx=20, pady=50)
exitbt.grid(row=4, column=1)


root.mainloop() 

