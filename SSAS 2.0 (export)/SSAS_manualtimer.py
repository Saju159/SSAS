import time
from tkinter import *
from tkinter import messagebox
import time
import datetime
from multiprocessing import Process


root = Tk()
root.geometry("300x250")
root.title("SSAS Manual Timer")

hour=StringVar()
minute=StringVar()
second=StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")



# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),
                textvariable=hour)
hourEntry.place(x=80,y=80)

minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                    textvariable=minute)
minuteEntry.place(x=130,y=80)

secondEntry= Entry(root, width=3, font=("Arial",18,""),
                    textvariable=second)
secondEntry.place(x=180,y=80)

textEntry= Entry(root, width=20, font=("Arial",18,""))
textEntry.place(x=20,y=5)

l = Label(root, text = "Set time to count towards: ")
l.config(font =("Courier", 10))
l.place(x=20,y=40)

k = Label(root, text = "h, min, sec")
k.config(font =("Courier", 10))
k.place(x=20,y=60)






def submit():  
    while 1 == 1:
        time.sleep(1)
        now = datetime.datetime.now()
        timehours = int(hourEntry.get())-now.hour
        timeminutes = int(minuteEntry.get())-now.minute
        timeseconds = int(secondEntry.get())-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        t -= 1
        l = Label(root, text = "Ajastin: " + timer2 )
        l.config(font =("Courier", 14))
        l.place(x=10, y=200)
        root.update()





btn = Button(root, text='Start Timer', bd='5',
            command= submit)
btn.place(x = 100,y = 120)


root.mainloop()