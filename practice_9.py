import turtle

window = turtle.Screen()
point = turtle.Turtle()

i = 100
while i > 0:
    point.forward(i)
    point.right(53)
    i -= 1
    # if i > 10:
        # point.forward(i)
        # point.right(90)



window.mainloop()