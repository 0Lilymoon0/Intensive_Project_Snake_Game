import pygame
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Snake')

################################################################################
# VARIABLES
################################################################################

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

CHARACTER_WIDTH = 10
CHARACTER_HEIGHT = 10

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player Variables
player_x = 50
player_y = 50

# Target Variables
target_x = random.random() * (SCREEN_WIDTH - CHARACTER_WIDTH)
target_y = random.random() * (SCREEN_WIDTH - CHARACTER_WIDTH)

# Other variables
velocity = 5
direction = "UP"
points = 0

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

################################################################################
# HELPER FUNCTIONS
################################################################################

def is_colliding(x1, y1, x2, y2, width, height):
    """Returns True if two rectangles are colliding, or False otherwise"""
    # If one rectangle is on left side of the other 
    if (x1 >= x2 + width) or (x2 >= x1 + width):
        return False
  
    # If one rectangle is above the other
    if (y1 >= y2 + height) or (y2 >= y1 + height):
        return False
  
    return True

def draw_text(text, color, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

################################################################################
# GAME LOOP
################################################################################

# Run until the user asks to quit
running = True
while running:

    # Advance the clock
    pygame.time.delay(20)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #
    if keys[pygame.K_LEFT]:
        direction = "LEFT"
    if keys[pygame.K_RIGHT]:
        direction = "RIGHT"
    if keys[pygame.K_UP]:
        direction = "UP"
    if keys[pygame.K_DOWN]:
        direction = "DOWN"

    # Update the player
    if direction == "LEFT":
        player_x -= velocity
    if direction == "RIGHT":
        player_x += velocity
    if direction == "UP":
        player_y -= velocity
    if direction == "DOWN":
        player_y += velocity

    # Quit the game if the player hits the edge of the screen
    if player_x < 0 or player_x > 500:
        pygame.quit()

    if player_y < 0 or player_y > 500:
        pygame.quit()

    # If player collides with target, reset it & increment points
    if is_colliding(player_x, player_y, target_x, target_y, CHARACTER_WIDTH, CHARACTER_HEIGHT):
        points += 100
        target_y = random.random() * (SCREEN_WIDTH - CHARACTER_WIDTH)
        target_x = random.random() * (SCREEN_WIDTH - CHARACTER_WIDTH)

    # Fill screen with white
    screen.fill(WHITE)

    # Draw the player as a green square
    pygame.draw.rect(screen, GREEN, (player_x, player_y, CHARACTER_WIDTH, CHARACTER_HEIGHT))

    # Draw the target as a red square
    pygame.draw.rect(screen, RED, (target_x, target_y, CHARACTER_WIDTH, CHARACTER_HEIGHT))

    # Draw the points
    draw_text(text=f'Points: {points}', color=BLACK, font_size=24, x=20, y=20)

    # Update the game display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()