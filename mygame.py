"""
For using Pygame library and must be added before any other pygame function,
else an initialization error may occur.
There are a couple of additional imports (random, time) that are used in Game.py
"""
import sys
import pygame
from pygame.locals import *  # pylint: disable=wildcard-import, unused-wildcard-import
from gamemodels import Player
from utility import load_image
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, BLACK

pygame.init()

FRAME_PER_SEC = pygame.time.Clock()

# Setting up Fonts
FONT = pygame.font.SysFont("Verdana", 60)
FONT_SMALL = pygame.font.SysFont("Verdana", 20)
GAME_OVER = FONT.render("Game Over", True, BLACK)

BACKGROUND = load_image("pitch640x484.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Setting up Sprites
P1 = Player()
# E1 = Enemy()

# Creating Sprites Groups
# enemies = pygame.sprite.Group()
# enemies.add(E1)
ALL_SPRITES = pygame.sprite.Group()
ALL_SPRITES.add(P1)
# all_sprites.add(E1)


# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(BACKGROUND, (0, 0))

# Moves and Re-draws all Sprites
    for entity in ALL_SPRITES:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.update()
