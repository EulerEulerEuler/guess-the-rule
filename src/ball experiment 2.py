# Place to experiment atm

from tkinter import *
from math import *

window = Tk()
window.title("hi!")

# make background
x_size = 750
y_size = 500
background = Canvas(window, width=x_size, height=y_size)
background.grid(row=0, column=0, rowspan=x_size, columnspan=y_size)
ball_size = 2
ball = Label(window, text="•", font='Courier, 30', width=ball_size, justify='center')
ball2 = Label(window, text="•", font='Courier, 30', width=ball_size, justify='center')

x_pos = 50
x2 = x_size - 50

while x_pos <= x_size - ball_size:
    window.after(10)
    x_pos += 1
    y_pos = round(y_size / 2 + sin(x_pos / 50) * 100)
    x2 -= 1
    y2 = round(y_size / 2 + cos(x_pos / 50) * 100)
    ball.grid(row=y_pos, column=x_pos)
    ball2.grid(row=y2, column=x_pos)
    window.update()

window.mainloop()
