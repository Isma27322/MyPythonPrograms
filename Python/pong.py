import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Initialize game variables
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

left_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2
right_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle_speed = 10

left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collisions with walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collisions with paddles
    if (
        ball_x <= PADDLE_WIDTH
        and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT
    ) or (
        ball_x >= WIDTH - PADDLE_WIDTH - BALL_RADIUS
        and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT
    ):
        ball_speed_x = -ball_speed_x

    # Check for a score
    if ball_x < 0:
        # Point for the right player
        right_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = -ball_speed_x
    elif ball_x > WIDTH:
        # Point for the left player
        left_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = -ball_speed_x

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (PADDLE_WIDTH, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(
        screen,
        WHITE,
        (WIDTH - PADDLE_WIDTH * 2, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT),
    )
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

    # Display scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 50))
    screen.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width(), 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
