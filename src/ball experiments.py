# Place to experiment atm

from tkinter import *
from math import *

window = Tk()

# make background
background = Canvas(window, width=5000, height=5000)
background.grid(row=0, column=0, rowspan=1000, columnspan=1000)

# structure grid
gridpoint1 = Label(text="")
gridpoint1.grid(row=0, column=0)
gridpoint2 = Label(text="")
gridpoint2.grid(row=9998, column=9998)

# make ball
# ball = Label(text="O")
x = 0
y = 500
r = 100
t = 0

while x < 1000:
    window.after(10)
    x += 10
    y = 100 + sqrt(100 + x**2)
    Label(text="•").grid(row=floor(y), column=floor(x))
    window.update()

# animate
while x < 10000:
    window.after(10)
    x += 1
    y = 100 + sin(x/10)*100
    Label(text="•").grid(row=floor(y), column=floor(x))
    window.update()

window.mainloop()
