import turtle
import random
import time

number_of_squares = int(input("How many squares would you like?"))

turtle.colormode(255)

My_turtle = turtle.Turtle()

My_turtle.speed(0)
turtle.bgcolor("black")
My_turtle.hideturtle()

i = 0

window_width = turtle.window_width() // 2 - 50
window_height = turtle.window_height() // 2 - 50

def Draw_Square_filled(Side_Length):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    My_turtle.color(r, g, b)
    My_turtle.pendown
    My_turtle.begin_fill()
    for side in range(4):
        My_turtle.forward(Side_Length)
        My_turtle.right(90)
    My_turtle.end_fill()
    My_turtle.penup()

for i in range(number_of_squares):
    size = random.randint(50,100)

    x = random.randint(-window_width, window_width)
    y = random.randint(-window_height, window_height)

    My_turtle.goto(x,y)

    Draw_Square_filled(size)

    

turtle.done()