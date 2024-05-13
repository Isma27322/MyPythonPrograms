import pygame
import math

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RAINBOW_COLORS = [(255, 0, 0), (255, 128, 0), (255, 255, 0),
                   (0, 255, 0), (0, 0, 255), (75, 0, 130), (127, 0, 255)]

# Define screen size
WIDTH = 800
HEIGHT = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainbow Spiral")

# Set starting position
x = WIDTH // 2
y = HEIGHT // 2

# Set initial radius and angle
radius = 5
angle = 0

# Set angle increment and color index
angle_increment = 0.1
color_index = 0

# Define growth factor for the spiral
growth_factor = 0.05

# Loop until user quits
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update angle and radius
    angle += angle_increment
    radius += radius * growth_factor

    # Calculate x and y offsets based on updated radius and angle
    x_offset = radius * math.cos(math.radians(angle))
    y_offset = radius * math.sin(math.radians(angle))

    # Choose the current color based on color index
    current_color = RAINBOW_COLORS[int(color_index % len(RAINBOW_COLORS))]

    # Draw the point
    pygame.draw.circle(screen, current_color, (x + x_offset, y + y_offset), 2)

    # Update the color index
    color_index += angle_increment * len(RAINBOW_COLORS)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
