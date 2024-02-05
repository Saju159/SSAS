#-----------------Maanantai-----------------------
ma1h = 9
ma1m = 45
ma1aine = "Psykologia"


ma2h = 11
ma2m = 15
ma2aine = "Äidinkieli"


ma3h = 12
ma3m = 45
ma3aine = "Fysiikka"


ma4h = 14
ma4m = 30
ma4aine = "Englanti"


ma5h = 16
ma5m = 00
ma5aine = "Musiikki"


#-------------Tiistai-------------
ti1h = 9
ti1m = 45
ti1aine = "Matematiikka"


ti2h = 11
ti2m = 15
ti2aine = "Matematiikka"


ti3h = 13
ti3m = 30
ti3aine = "Englanti"


ti4h = 15
ti4m = 00
ti4aine = "Musiikki"


#-------------Keskiviikko-------------
ke1h = 9
ke1m = 45
ke1aine = "Matematiikka"


ke2h = 11
ke2m = 15
ke2aine = "Äidinkieli"


ke3h = 13
ke3m = 30
ke3aine = "Fysiikka"


ke4h = 15
ke4m = 00
ke4aine = "Psykologia"


#-------------Torstai-------------
#to1h = 9
to1h = 22
to1m = 45
to1aine = "Musiikki"


to2h = 11
to2m = 15
to2aine = "Englanti"


to3h = 12
to3m = 45
to3aine = "Matematiikka"


to4h = 14
to4m = 30
to4aine = "Fysiikka"


#-------------Perjantai-------------
pe1h = 9
pe1m = 45
pe1aine = "Matematiikka"


pe2h = 11
pe2m = 15
pe2aine = "Äidinkieli"


pe3h = 13
pe3m = 30
pe3aine = "Matematiikka"


pe4h = 15
pe4m = 00
pe4aine = "Psykologia"




# import the time module
import time
from datetime import datetime
import datetime
from time import sleep
import webbrowser
from tkinter import *
from multiprocessing import Process





timerwindow = Tk()
timerwindow.title("SSAS Timers")
lbl = Label(timerwindow, text="SSAS Timers")
timerwindow.geometry('400x200')
timerwindow.configure(bg='gray')



now = datetime.datetime.now()
weekday1 = (now.strftime("%w"))
weekday2 = int(weekday1)
#weekday2 = 1

#print (now.hour)

#-------------Maanantai------------------------------------------------------------------
if weekday2 == 1:
    while 1 == 1:
        now = datetime.datetime.now()
        time.sleep(1)

        k = Label(timerwindow, text = now)
        k.config(font =("Courier", 14))
        k.place(x=10, y=160)


        timehours = ma1h-now.hour
        timeminutes = ma1m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ma1aine + ("loppuu:  ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=10)




        timehours = ma2h-now.hour
        timeminutes = ma2m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ma2aine + ("loppuu:  ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=40)


        timehours = ma3h-now.hour
        timeminutes = ma3m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ma3aine + ("loppuu:  ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=70)

        timehours = ma4h-now.hour
        timeminutes = ma4m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ma4aine + ("loppuu:  ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=100)



        timehours = ma5h-now.hour
        timeminutes = ma5m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ma5aine + ("loppuu:  ") + timer2)
        print(timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=130)
            



#-------------Tiistai------------------------------------------------------------------
if weekday2 == 2:


    
    while 1 == 1:
        now = datetime.datetime.now()
        time.sleep(1)

        k = Label(timerwindow, text = now)
        k.config(font =("Courier", 14))
        k.place(x=10, y=160)

        timehours = ti1h-now.hour
        timeminutes = ti1m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ti1aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=10)



        timehours = ti2h-now.hour
        timeminutes = ti2m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ti2aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=40)



        timehours = ti3h-now.hour
        timeminutes = ti3m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ti3aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=70)



        timehours = ti4h-now.hour
        timeminutes = ti4m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ti4aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=100)


#-------------Keskiviikko------------------------------------------------------------------
if weekday2 == 3:


    
    while 1 == 1:
        now = datetime.datetime.now()
        time.sleep(1)

        k = Label(timerwindow, text = now)
        k.config(font =("Courier", 14))
        k.place(x=10, y=160)

        timehours = ke1h-now.hour
        timeminutes = ke1m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ke1aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=10)



        timehours = ke2h-now.hour
        timeminutes = ke2m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ke2aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=40)



        timehours = ke3h-now.hour
        timeminutes = ke3m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ke3aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=70)



        timehours = ke4h-now.hour
        timeminutes = ke4m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = ke4aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=100)


#-------------Torstai------------------------------------------------------------------
if weekday2 == 4:

    
    while 1 == 1:
        now = datetime.datetime.now()
        time.sleep(1)

        k = Label(timerwindow, text = now)
        k.config(font =("Courier", 14))
        k.place(x=10, y=160)

        timehours = to1h-now.hour
        timeminutes = to1m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = to1aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=10)



        timehours = to2h-now.hour
        timeminutes = to2m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = to2aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=40)



        timehours = to3h-now.hour
        timeminutes = to3m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = to3aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=70)



        timehours = to4h-now.hour
        timeminutes = to4m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = to4aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=100)


#-------------Perjantai------------------------------------------------------------------

if weekday2 == 5:

    
    while 1 == 1:
        now = datetime.datetime.now()
        time.sleep(1)

        k = Label(timerwindow, text = now)
        k.config(font =("Courier", 14))
        k.place(x=10, y=160)

        timehours = pe1h-now.hour
        timeminutes = pe1m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = pe1aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=10)



        timehours = pe2h-now.hour
        timeminutes = pe2m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = pe2aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=40)



        timehours = pe3h-now.hour
        timeminutes = pe3m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = pe3aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=70)



        timehours = pe4h-now.hour
        timeminutes = pe4m-now.minute
        timeseconds = 00-now.second
        t = (int(timehours) * 60 * 60) + (int(timeminutes) * 60) + int((timeseconds))
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer2 = '{:02d}:{:02d}:{:02}'.format(hours, mins, secs)
        timerwindow.update()
        t -= 1
        l = Label(timerwindow, text = pe4aine + ("loppuu: ") + timer2)
        l.config(font =("Courier", 14))
        l.place(x=10, y=100)



#-------------Lauantai------------------------------------------------------------------

if weekday2 == 6:
    l = Label(timerwindow, text = "Ei koulua")
    l.config(font =("Courier", 14))
    l.place(x=10, y=10)

#-------------Sunnuntai------------------------------------------------------------------

if weekday2 == 0:
    l = Label(timerwindow, text = "Ei koulua")
    l.config(font =("Courier", 14))
    l.place(x=10, y=10)






timerwindow.mainloop()





        
