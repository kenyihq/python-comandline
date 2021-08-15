import turtle

window = turtle.Screen()
tortuga = turtle.Turtle()

window.screensize(400, 400 , "white")

tortuga.pensize(2)

tortuga.color("red")

x = 20
y = 400
cambio = 20

for x in range(x,400 + cambio,cambio):
    tortuga.goto(x, 0)
    tortuga.goto(0, y)
    y = y - cambio
    tortuga.goto(0, y)


tortuga.color("black")
tortuga.forward(400)
tortuga.left(90)
tortuga.forward(400)
tortuga.left(90)
tortuga.forward(400)
tortuga.left(90)
tortuga.forward(400)

turtle.done()
window.mainloop()