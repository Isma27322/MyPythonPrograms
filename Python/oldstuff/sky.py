import turtle
import random

# Get the number of stars from user input
numOfStars = input("How many stars would you like? (Default is 100): ")

# Set the default value to 100 if the user input is empty
if numOfStars == "":
    numOfStars = 100
else:
    numOfStars = int(numOfStars)

turtle.colormode(255)

# Create turtle object
my_turtle = turtle.Turtle()

# Set initial speed and background color
my_turtle.speed(0)
turtle.bgcolor("black")


# Define colors for the stars
#colors = ["white", "yellow", "cyan", "magenta", "orange", "lime", "red", "blue", "purple", "green", "pink"]

# Get the dimensions of the Turtle graphics window
window_width = turtle.window_width() // 2 - 50
window_height = turtle.window_height() // 2 - 50

# Draw stars
for i in range(1,numOfStars + 1):
    x = random.randint(-window_width, window_width)
    y = random.randint(-window_height, window_height)

    # Draw the star
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()


    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_turtle.color(r, g, b)


#    my_turtle.color(random.choice(colors))
    my_turtle.begin_fill()
    for _ in range(5):
        my_turtle.forward(100)
        my_turtle.right(144)
    my_turtle.end_fill()
    if i % 10 == 0:
        print(i)

# Hide the turtle
my_turtle.hideturtle()

# Exit on click
turtle.done()
