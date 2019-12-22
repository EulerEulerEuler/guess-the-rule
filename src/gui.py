# Place to experiment atm

from tkinter import *
from math import *

window = Tk()

# make background
background = Canvas(window, width=500, height=500)
background.grid(row=0, column=0, rowspan=100, columnspan=100)

# entrybox
entry = Entry(text = "Enter text here")
entry.grid(row=0, column=0)

window.mainloop()
