import turtle
import random

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed

# Define colors for a vibrant palette
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Function to draw a spiral with a random color and size
def draw_spiral(size):
    t.pencolor(random.choice(colors))
    for i in range(size):
        t.forward(i * 2)
        t.right(90)

# Function to draw a star with a random color and size
def draw_star(size):
    t.pencolor(random.choice(colors))
    for i in range(5):
        t.forward(size)
        t.right(144)

# Create a captivating pattern of spirals and stars
for i in range(30):
    angle = random.randint(0, 360)
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    t.setheading(angle)

    if random.random() > 0.5:
        draw_spiral(random.randint(50, 150))
    else:
        draw_star(random.randint(50, 150))

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
