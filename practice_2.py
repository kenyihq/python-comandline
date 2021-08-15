import turtle
import tkinter as ttk
from tkinter import *
from tkinter.colorchooser import *

window = turtle.Screen()
tortuga = turtle.Turtle()
tortuga.pensize(3)

def going_home():
	tortuga.penup()
	tortuga.home()
	tortuga.pendown()

def turning_left():
	tortuga.left(30)

def turning_right():
	tortuga.right(30)

def drawing():
	tortuga.forward(30)

def pen_up():
	tortuga.penup()

def pen_pendown():
	tortuga.pendown()

def geting_color():
	tortuga.pencolor(askcolor()[1])

root = Tk()
root.title('Turtle Control Panel')

go_home_button = ttk.Button(root, text="⌂", font=('',18), command=going_home).grid(column = 0, row= 0)

turn_left_button = ttk.Button(root, text="↺", font=('',18), command=turning_left).grid(column = 1, row= 0)

turn_right_button = ttk.Button(root, text="↻", font=('',18), command=turning_right)	.grid(column = 2, row= 0)

draw_button = ttk.Button(root, text="→", font=('',18), command=drawing)	.grid(column = 3, row= 0)

pen_up_button = ttk.Button(root, text="○", font=('',18), command=pen_up).grid(column = 4, row= 0)

pen_pendown_button = ttk.Button(root, text="●", font=('',18), command=pen_pendown).grid(column = 5, row= 0)

color_button = ttk.Button(root, text="☺", font=('',18), command=geting_color).grid(column = 6, row= 0)

window.mainloop()