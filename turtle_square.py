# import turtle


# window = turtle.Screen()
# tortuga = turtle.Turtle()

# i = 0
# # while i < 4:
# #     tortuga.forward(100)
# #     tortuga.right(95)
# #     i += 1

# while i < 3:
#     tortuga.forward(200)
#     tortuga.right(120)
#     i += 1

# # tortuga.forward(100)
# # tortuga.right(90)

# # tortuga.forward(100)
# # tortuga.right(90)

# # tortuga.forward(100)
# # tortuga.right(90)

# window.mainloop()


import turtle

window = turtle.Screen()

colors=['red','purple','blue','green','yellow','orange']

t = turtle.Pen()
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.mainloop()

