import turtle

# Create turtle object
my_turtle = turtle.Turtle()

# Set initial speed and background color
my_turtle.speed(0)
turtle.bgcolor("black")

# Define colors for the spiral
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the spiral
for i in range(400):
    my_turtle.color(colors[i % len(colors)])
    my_turtle.forward(i)
    my_turtle.left(59)

# Hide the turtle
my_turtle.hideturtle()

# Exit on click
turtle.done()
