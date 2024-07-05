import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fruit Catcher')

# Basket setup
basket_width = 100
basket_height = 20
basket_x = (screen_width - basket_width) // 2
basket_y = screen_height - basket_height - 10
basket_speed = 10

# Fruit setup
fruit_width = 30
fruit_height = 30
fruit_speed = 5
fruit_frequency = 25  # Higher value means lower frequency of fruits

# Game variables
score = 0
missed_fruits = 0
max_missed_fruits = 5

# Font setup
font = pygame.font.SysFont(None, 55)


def display_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])


# Main game loop
running = True
fruits = []
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
        basket_x += basket_speed

    # Add new fruit
    if random.randint(1, fruit_frequency) == 1:
        fruit_x = random.randint(0, screen_width - fruit_width)
        fruits.append([fruit_x, 0])

    # Move fruits
    for fruit in fruits:
        fruit[1] += fruit_speed

    # Check for catching fruits
    for fruit in fruits[:]:
        if fruit[1] > screen_height:
            fruits.remove(fruit)
            missed_fruits += 1
        elif basket_y < fruit[1] + fruit_height and basket_x < fruit[0] + fruit_width and basket_x + basket_width > \
                fruit[0]:
            fruits.remove(fruit)
            score += 1

    # Game over condition
    if missed_fruits >= max_missed_fruits:
        running = False

    # Drawing
    screen.fill(white)
    pygame.draw.rect(screen, black, [basket_x, basket_y, basket_width, basket_height])
    for fruit in fruits:
        pygame.draw.ellipse(screen, red, [fruit[0], fruit[1], fruit_width, fruit_height])

    display_text(f'Score: {score}', black, 10, 10)
    display_text(f'Missed: {missed_fruits}', black, 10, 50)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
