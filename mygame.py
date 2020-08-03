"""
For using Pygame library and must be added before any other pygame function,
else an initialization error may occur.
There are a couple of additional imports (random, time) that are used in Game.py
"""
import sys
import pygame
from pygame.locals import *  # pylint: disable=wildcard-import, unused-wildcard-import


pygame.init()

# pylint: disable=pointless-string-statement

# Setting up FPS
FPS = 60
FRAME_PER_SEC = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 484
SCREEN_HEIGHT = 640
SPEED = 5
SCORE = 0

# Setting up Fonts
FONT = pygame.font.SysFont("Verdana", 60)
FONT_SMALL = pygame.font.SysFont("Verdana", 20)
GAME_OVER = FONT.render("Game Over", True, BLACK)


""" TASK Create background & import
This path function is used for saving time and space, not having to type out or paste path
"""
ASSETS_PATH = 'C:/Users/46707/Work/firstgame/Import_files'

BACKGROUND = pygame.image.load("{}/pitch640x484.png".format(ASSETS_PATH))


# Create a white screen
DISPLAYSURF = pygame.display.set_mode((640, 484))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(BACKGROUND, (0, 0))
