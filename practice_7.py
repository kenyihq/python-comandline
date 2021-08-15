import turtle

window=turtle.Screen() 
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.fillcolor("pink")

tortuga.begin_fill()

for i in range(36):
	tortuga.left(10)
	for i in range(4):
		tortuga.forward(200)
		tortuga.right(90)

tortuga.end_fill()
window.mainloop()