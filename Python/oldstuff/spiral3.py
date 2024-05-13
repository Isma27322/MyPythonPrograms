import pygame
import math

# Define colors using RGB values (add more for additional colors)
rainbow_colors = [
    (255, 0, 0),  # Red
    (255, 128, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),  # Green
    (0, 128, 255),  # Teal
    (0, 0, 255),  # Blue
    (75, 0, 130),  # Purple
    (128, 0, 255),  # Violet
]

# Define screen size
WIDTH = 800
HEIGHT = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainbow Spiral")

# Set initial position to the center of the screen
x = WIDTH // 2
y = HEIGHT // 2

# Set initial radius and angle
radius = 1
angle = 0

# Define angle increment and color index
angle_increment = 5
color_index = 0

# Define maximum radius and radius growth factor
max_radius = 100
radius_growth_factor = 0.005

# Loop until user quits
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Update angle and radius
    angle += angle_increment

    if radius < max_radius:
        radius += radius * radius_growth_factor

    # Calculate initial offset
    x_offset = radius * math.cos(math.radians(angle)) + x
    y_offset = radius * math.sin(math.radians(angle)) + y

    # Choose the current color based on color index
    current_color = rainbow_colors[color_index % len(rainbow_colors)]

    # Draw a circle using the current color
    pygame.draw.circle(screen, current_color, (x_offset, y_offset), radius, 0)

    # Update the color index
    color_index += 1

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
