from tkinter import *
import tkinter as tk
import io
from sys import exit
import time

window = Tk()
window.title("SSAS Settings")
lbl = Label(window, text="SSAS")
window.geometry('350x200')
window.configure(bg='gray')


time.sleep(1)

file = open('booksettings.txt', "r")
bcontents = file.read()
openallbooks = int(bcontents)
def bsetting():
    if int(bcontents) == 1:
        file = open('booksettings.txt', "w")
        file.write("0")
        file.close()
        exit(0)
    if int(bcontents) == 0:
        file = open('booksettings.txt', "w")
        file.write("1")
        file.close()
        exit(0)
file.close()


file = open('wilmasettings.txt', "r")
wcontents = file.read()
openwilma = int(wcontents)
def wsetting():
    if int(wcontents) == 1:
        file = open('wilmasettings.txt', "w")
        file.write("0")
        file.close()
        exit(0)
    if int(wcontents) == 0:
        file = open('wilmasettings.txt', "w")
        file.write("1")
        file.close()
        exit(0)
file.close()


file = open('icloudsettings.txt', "r")
icontents = file.read()
openicloud = int(icontents)
def isetting():
    if int(icontents) == 1:
        file = open('icloudsettings.txt', "w")
        file.write("0")
        file.close()
        exit(0)
    if int(icontents) == 0:
        file = open('icloudsettings.txt', "w")
        file.write("1")
        file.close()
        exit(0)
file.close()






c1 = tk.Checkbutton(window, text='Open all books at a time',variable=openallbooks, onvalue=1, offvalue=0,command=bsetting)
c1.pack()

c2 = tk.Checkbutton(window, text='Open wilma when opening books',variable=openwilma, onvalue=1, offvalue=0,command=wsetting)
c2.place(x=10, y=40)
c2.pack()

c3 = tk.Checkbutton(window, text='Open iCloud when opening books',variable=openicloud, onvalue=1, offvalue=0,command=isetting)
c3.place(x=10, y=80)
c3.pack()

if int(bcontents) == 1:
    c1.select()

if int(wcontents) == 1:
    c2.select()

if int(icontents) == 1:
    c3.select()



window.mainloop()