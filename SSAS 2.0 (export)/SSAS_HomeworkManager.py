 # Import
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import sys


# Setup Variables

appName = 'SSAS Homework Manager'
nofileOpenedString = 'Homework.txt'

currentFilePath = nofileOpenedString

# Viable File Types, when opening and saving files.
fileTypes = [("Text Files","*.txt"), ("Markdown","*.md")]

# Tkinter Setup
window = Tk()

# Set the first column to occupy 100% of the width
window.grid_columnconfigure(0, weight=1)

window.title(appName + " - " + currentFilePath)

# Window Dimensions in Pixel
window.geometry('500x400')


# Handler Functions
def fileDropDownHandeler(action):
    global currentFilePath


    # Opening a File
    if action == "open":
        file = filedialog.askopenfilename(filetypes = fileTypes)

        window.title(appName + " - " + file)

        currentFilePath = file



def textchange(event):

    with open('homework.txt', 'w') as f:
            f.write(txt.get('1.0','end'))


# Widgets

# Text Area
txt = scrolledtext.ScrolledText(window, height=999)
txt.grid(row=1,sticky=N+S+E+W)


with open('homework.txt', 'r') as f:
            txt.delete(1.0,END)
            txt.insert(INSERT,f.read())


# Bind event in the widget to a function
txt.bind('<KeyPress>', textchange)
# Menu
menu = Menu(window)
# Set Menu to be Main Menu
window.config(menu=menu)

# Enabling "open with" by looking if the second argument was passed.
if len(sys.argv) == 2:
    currentFilePath = sys.argv[1]

    window.title(appName + " - " + currentFilePath)

    with open(currentFilePath, 'r') as f:
        txt.delete(1.0,END)
        txt.insert(INSERT,f.read())

# Main Loop
window.mainloop()

