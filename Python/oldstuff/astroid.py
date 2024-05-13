import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up player
player_size = 50
player_x = width // 2
player_y = height // 2
player_speed = 5

# Set up asteroids
asteroids = []
num_asteroids = 5
asteroid_speed = 2

for _ in range(num_asteroids):
    asteroid_size = random.randint(20, 50)
    asteroid_x = random.randint(0, width)
    asteroid_y = random.randint(0, height)
    asteroid_angle = random.uniform(0, 2 * math.pi)
    asteroids.append((asteroid_x, asteroid_y, asteroid_size, asteroid_angle))

# Set up clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < height - player_size:
        player_y += player_speed

    # Update asteroids
    for i in range(num_asteroids):
        asteroid_x, asteroid_y, asteroid_size, asteroid_angle = asteroids[i]

        # Move asteroid
        asteroid_x += asteroid_speed * math.cos(asteroid_angle)
        asteroid_y += asteroid_speed * math.sin(asteroid_angle)

        # Wrap around the screen
        if asteroid_x < 0:
            asteroid_x = width
        elif asteroid_x > width:
            asteroid_x = 0

        if asteroid_y < 0:
            asteroid_y = height
        elif asteroid_y > height:
            asteroid_y = 0

        asteroids[i] = (asteroid_x, asteroid_y, asteroid_size, asteroid_angle)

    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for asteroid in asteroids:
        asteroid_rect = pygame.Rect(asteroid[0], asteroid[1], asteroid[2], asteroid[2])
        if player_rect.colliderect(asteroid_rect):
            print("Game Over!")
            running = False

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

    for asteroid in asteroids:
        pygame.draw.circle(screen, white, (int(asteroid[0]), int(asteroid[1])), asteroid[2])

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
