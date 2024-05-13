import turtle
import random

# Function to draw a star
def draw_star(size, color):
    angle = 120
    turtle.fillcolor(color)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()

# Set up the screen
turtle.bgcolor("black")
turtle.speed('fastest')

# Draw multiple stars
colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white']
for i in range(50):
    turtle.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    turtle.goto(x, y)
    turtle.pendown()
    draw_star(random.randint(10, 30), random.choice(colors))

# Hide the turtle and display the result
turtle.hideturtle()
turtle.done()
