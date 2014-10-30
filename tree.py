import turtle

def tree (turtle, n, size):
	turtle.forward(size)

	if n == 0:
		turtle.forward(-size)
		return

	for props in [[60, size / 2], [-45, size / 4], [-45, size / 2], [30, 0]]:
		turtle.left(props[0])
		if props[1] == 0:
			continue
		tree(turtle, n-1, props[1])

	turtle.forward(-size)

alex = turtle.Turtle()
alex.left(90)
alex.forward(-500)
alex.speed(0)
alex.hideturtle()

wn = turtle.Screen()
wn.delay(0)

tree(alex, 10, 600)

wn.mainloop()