import webbrowser
from tkinter import *
window = Tk()
import os
import subprocess
from multiprocessing import Process

window.title("SSAS")
lbl = Label(window, text="SSAS")
window.geometry('350x200')
window.configure(bg='gray')





def loop_a():
    os.system('python SSAS_timer.py')

def loop_b():
    os.system('python SSAS_books.py')

def loop_c():
    os.system('python SSAS_manualtimer.py')

def loop_d():
    os.system('python SSAS_HomeworkManager.py')

def loop_e():
    os.system('python SSAS_settings.py')


def Starttimers():
    Process(target=loop_a).start()
 
def openbooks():    
    Process(target=loop_b).start()

def manualtimer():
    Process(target=loop_c).start()

def homeworkmanager():
    Process(target=loop_d).start()

def settings():
    Process(target=loop_e).start()
    



    
#master = Tk()
button1=Button(window, text="Start Timers",bg="yellow", command=Starttimers)
button1.place(x=10, y=10)

button2=Button(window, text="Open Books",bg="orange", command=openbooks)
button2.place(x=111, y=10)

button3=Button(window, text="Manual Timer",bg="green", command=manualtimer)
button3.place(x=210, y=10)

button4=Button(window, text="Homework Manager",bg="cyan", command=homeworkmanager)
button4.place(x=180, y=45)

button6=Button(window, text="Open Settings",bg="grey", command=settings)
button6.place(x=10, y=160)









window.mainloop()
