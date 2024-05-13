import turtle

# Define colors
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Define screen size and background color
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Create and configure the turtle
t = turtle.Turtle()
t.speed(0)  # Set turtle speed to maximum
t.penup()  # Lift the pen to avoid drawing an initial line
t.goto(0, 0)  # Move the turtle to the center
t.pendown()  # Put the pen down to start drawing

# Define initial radius and angle increment
radius = 1  # Decrease for even tighter spiral
angle_increment = 5  # Increase for even tighter spiral

# Define maximum radius and radius growth factor
max_radius = 100  # Reduce for even tighter spiral
radius_growth_factor = 0.005  # Decrease for slower growth

# Loop to draw the spiral
while radius < max_radius:
    # Choose the current color based on the angle
    color_index = int(t.heading() / 360 * len(rainbow_colors))
    t.pencolor(rainbow_colors[color_index])

    # Draw a line segment based on the current radius
    t.forward(radius)

    # Increase the angle and update the radius for the next iteration
    t.left(angle_increment)
    radius += radius_growth_factor

# Keep the turtle window open until closed by the user
screen.exitonclick()
