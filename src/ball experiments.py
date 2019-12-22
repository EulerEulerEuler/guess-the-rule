# Place to experiment atm

from tkinter import *
from math import *

window = Tk()

# make background
background = Canvas(window, width=500, height=500)
background.grid(row=0, column=0, rowspan=1000, columnspan=1000)

# make ball
ball = Label(text="O")
x = 1000
y = 1000
r = 100
t = 0

# animate
while x < 100:
    window.after(10)
    t += 1
    # x = 1
    y = floor(t**2)
    ball.grid(row=x, column=y)
    window.update()

window.mainloop()
