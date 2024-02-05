#-------------Maanantai-------------
ma1digikirja = "https://digioppikirja.fi/?d=code_user_has_used#omat-kirjat"
ma2digikirja = "https://alyapp.fi/#/payment"
ma3digikirja = "https://opiskelija.otava.fi/login"
ma4digikirja = "https://opiskelija.otava.fi/login"
ma5digikirja = "https://www.google.com/"

#-------------Tiistai-------------
ti1digikirja = "https://kampus.sanomapro.fi/content-feed/67ec6350-4e21-49a0-b1f2-81393502a324/es:ED69922C-1F8A-40B0-A7B0-979A8F667DDD"
ti2digikirja = "https://kampus.sanomapro.fi/content-feed/67ec6350-4e21-49a0-b1f2-81393502a324/es:ED69922C-1F8A-40B0-A7B0-979A8F667DDD"
ti3digikirja = "https://opiskelija.otava.fi/login"
ti4digikirja = "https://www.google.com/"

#-------------Keskiviikko-------------
ke1digikirja = "https://kampus.sanomapro.fi/content-feed/67ec6350-4e21-49a0-b1f2-81393502a324/es:ED69922C-1F8A-40B0-A7B0-979A8F667DDD"
ke2digikirja = "https://alyapp.fi/#/payment"
ke3digikirja = "https://opiskelija.otava.fi/login"
ke4digikirja = "https://digioppikirja.fi/?d=code_user_has_used#omat-kirjat"

#-------------Torstai-------------
to1digikirja = "https://www.google.com/"
to2digikirja = "https://opiskelija.otava.fi/login"
to3digikirja = "https://kampus.sanomapro.fi/content-feed/67ec6350-4e21-49a0-b1f2-81393502a324/es:ED69922C-1F8A-40B0-A7B0-979A8F667DDD"
to4digikirja = "https://opiskelija.otava.fi/login"

#-------------Perjantai-------------
pe1digikirja = "https://kampus.sanomapro.fi/content-feed/67ec6350-4e21-49a0-b1f2-81393502a324/es:ED69922C-1F8A-40B0-A7B0-979A8F667DDD"
pe2digikirja = "https://alyapp.fi/#/payment"
pe3digikirja = "https://kampus.sanomapro.fi/content-feed/67ec6350-4e21-49a0-b1f2-81393502a324/es:ED69922C-1F8A-40B0-A7B0-979A8F667DDD"
pe4digikirja = "https://digioppikirja.fi/?d=code_user_has_used#omat-kirjat"


import time
from datetime import datetime
import datetime
from time import sleep
import webbrowser


file = open('wilmasettings.txt', "r")
wcontents = file.read()
file.close()

file = open('booksettings.txt', "r")
bcontents = file.read()
file.close()

file = open('icloudsettings.txt', "r")
icontents = file.read()
file.close()

now = datetime.datetime.now()
time = (now.hour * 60) + now.minute
weekday1 = (now.strftime("%w"))
weekday2 = int(weekday1)

#time = 800
#weekday2 = 4

chour= 12
cminute= 15
ctime = (chour*60) + cminute

print(ctime)

if weekday2 == 1:
    if int(wcontents) == 1:
        webbrowser.open_new_tab("https://kotka.inschool.fi/")
    if int(icontents) == 1:
        webbrowser.open_new_tab("https://www.icloud.com/notes/0db26Z6bpf5U8M-WdT-sG1EYg")

    if time > 510 and time < 585 or int(bcontents) == 1:
        webbrowser.open_new_tab(ma1digikirja)
    if time > 600 and time < 675 or int(bcontents) == 1:
        webbrowser.open_new_tab(ma2digikirja)
    if time > 681 and time < 765 or int(bcontents) == 1:
        webbrowser.open_new_tab(ma3digikirja)
    if time > 766 and time < 870 or int(bcontents) == 1:
        webbrowser.open_new_tab(ma4digikirja)
    if time > 871 and time < 960 or int(bcontents) == 1:
        webbrowser.open_new_tab(ma5digikirja)


if weekday2 == 2:
    if int(wcontents) == 1:
        webbrowser.open_new_tab("https://kotka.inschool.fi/")
    if int(icontents) == 1:
        webbrowser.open_new_tab("https://www.icloud.com/notes/0db26Z6bpf5U8M-WdT-sG1EYg")

    if time > 510 and time < 585 or int(bcontents) == 1:
        webbrowser.open_new_tab(ti1digikirja)
    if time > 586 and time < 675 or int(bcontents) == 1:
        webbrowser.open_new_tab(ti2digikirja)
    if time > 730 and time < 800 or int(bcontents) == 1:
        webbrowser.open_new_tab(ti3digikirja)
    if time > 801 and time < 900 or int(bcontents) == 1:
        webbrowser.open_new_tab(ti4digikirja)


if weekday2 == 3:
    if int(wcontents) == 1:
        webbrowser.open_new_tab("https://kotka.inschool.fi/")
    if int(icontents) == 1:
        webbrowser.open_new_tab("https://www.icloud.com/notes/0db26Z6bpf5U8M-WdT-sG1EYg")

    if time > 510 and time < 585 or int(bcontents) == 1:
        webbrowser.open_new_tab(ke1digikirja)
    if time > 586 and time < 675 or int(bcontents) == 1:
        webbrowser.open_new_tab(ke2digikirja)
    if time > 730 and time < 800 or int(bcontents) == 1:
        webbrowser.open_new_tab(ke3digikirja)
    if time > 801 and time < 900 or int(bcontents) == 1:
        webbrowser.open_new_tab(ke4digikirja)


if weekday2 == 4:
    if int(wcontents) == 1:
        webbrowser.open_new_tab("https://kotka.inschool.fi/")
    if int(icontents) == 1:
        webbrowser.open_new_tab("https://www.icloud.com/notes/0db26Z6bpf5U8M-WdT-sG1EYg")

    if time > 510 and time < 585 or int(bcontents) == 1:
        webbrowser.open_new_tab(to1digikirja)
    if time > 600 and time < 675 or int(bcontents) == 1:
        webbrowser.open_new_tab(to2digikirja)
    if time > 681 and time < 765 or int(bcontents) == 1:
        webbrowser.open_new_tab(to3digikirja)
    if time > 766 and time < 870 or int(bcontents) == 1:
        webbrowser.open_new_tab(to4digikirja)


if weekday2 == 5:
    if int(wcontents) == 1:
        webbrowser.open_new_tab("https://kotka.inschool.fi/")
    if int(icontents) == 1:
        webbrowser.open_new_tab("https://www.icloud.com/notes/0db26Z6bpf5U8M-WdT-sG1EYg")

    if time > 510 and time < 585 or int(bcontents) == 1:
        webbrowser.open_new_tab(pe1digikirja)
    if time > 586 and time < 675 or int(bcontents) == 1:
        webbrowser.open_new_tab(pe2digikirja)
    if time > 730 and time < 800 or int(bcontents) == 1:
        webbrowser.open_new_tab(pe3digikirja)
    if time > 801 and time < 900 or int(bcontents) == 1:
        webbrowser.open_new_tab(pe4digikirja)

