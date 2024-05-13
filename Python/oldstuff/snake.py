import pygame
import sys
import random

# Function to get user input for amount of food and initial snake length
def get_user_input():
    num_food = int(input("Enter the amount of food you want: "))
    while num_food <= 0 or num_food > 70000:
        print("Invalid input. Please enter a number between 1 and 70000.")
        num_food = int(input("Enter the amount of food you want: "))

    snake_length = int(input("Enter the initial length of the snake: "))
    while snake_length <= 0 or snake_length >= 41:
        print("Invalid input. Please enter a number between 1 and 40.")
        snake_length = int(input("Enter the initial length of the snake: "))

    return num_food, snake_length


num_food, snake_length = get_user_input()

# Initialize Pygame
pygame.init()

# Set up game constants
screen_width = 1300
screen_height = 550
grid_size = 10
direction = "right"
score = 0

# Set up colors
dark_gray = (50, 50, 50)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
light_gray = (200, 200, 200)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up the snake
snake = [{"x": 0, "y": 0}] * snake_length

# Set up the food
food = [{"x": 0, "y": 0} for _ in range(num_food)]

# Generate initial food positions
for i in range(num_food):
    food[i]["x"] = random.randint(0, screen_width // grid_size - 1) * grid_size
    food[i]["y"] = random.randint(0, screen_height // grid_size - 1) * grid_size

def generate_food(f):
    max_x = screen_width // grid_size
    max_y = screen_height // grid_size
    f["x"] = random.randint(0, max_x - 1) * grid_size
    f["y"] = random.randint(0, max_y - 1) * grid_size

def draw(screen):
    # Clear the screen
    screen.fill(black)

    # Draw the game board
    for x in range(0, screen_width, grid_size):
        for y in range(0, screen_height, grid_size):
            pygame.draw.rect(screen, dark_gray, (x, y, grid_size, grid_size))

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, green, (segment["x"], segment["y"], grid_size, grid_size))

    # Draw the food
    for f in food:
        pygame.draw.rect(screen, red, (f["x"], f["y"], grid_size, grid_size))

    # Draw the score
    score_text = font.render("Score: {}".format(score), True, light_gray)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

def update():
    global score

    # Move the snake
    head = {"x": snake[0]["x"], "y": snake[0]["y"]}
    if direction == "right":
        head["x"] += grid_size
    elif direction == "left":
        head["x"] -= grid_size
    elif direction == "up":
        head["y"] -= grid_size
    elif direction == "down":
        head["y"] += grid_size
    snake.insert(0, head)

    # Check for collision with food
    for f in food:
        if head["x"] == f["x"] and head["y"] == f["y"]:
            score += 1
            generate_food(f)  # Pass the specific food item to move
        else:
            if len(snake) > snake_length:
                snake.pop()

    # Check for collision with walls
    if (
        head["x"] < 0
        or head["x"] >= screen_width
        or head["y"] < 0
        or head["y"] >= screen_height
    ):
        game_over()

    # Check for collision with itself
    for segment in snake[1:]:
        if head["x"] == segment["x"] and head["y"] == segment["y"]:
            game_over()

def game_over():
    global score
    print("Game over! Your score was", score)
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        reset_game()
    else:
        print("See you next time!")
        pygame.quit()
        

def reset_game():
    global snake, score
    snake = [{"x": 0, "y": 0}] * snake_length
    score = 0
    for f in food:
        generate_food(f)


# Main game loop
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game small easy")
pygame.display.flip()  # Update the display immediately to bring the window to the front

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"

    update()
    draw(screen)
    clock.tick(10)  # Adjust the speed of the game
