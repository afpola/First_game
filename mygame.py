"""
For using Pygame library and must be added before any other pygame function,
else an initialization error may occur.
There are a couple of additional imports (random, time) that are used in Game.py
"""
import sys
import pygame
from pygame import sprite, display, time, font, event
from pygame.locals import *  # pylint: disable=wildcard-import, unused-wildcard-import
from gamemodels import Player, Goalkeeper, Ball
from utility import load_image
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, BLACK

pygame.init()

FRAME_PER_SEC = time.Clock()

# Setting up Fonts
FONT = font.SysFont("Verdana", 60)
FONT_SMALL = font.SysFont("Verdana", 20)
GAME_OVER = FONT.render("Game Over", True, BLACK)

BACKGROUND = load_image("pitch640x484.png")

# Create a white screen
DISPLAYSURF = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
display.set_caption("Game")

# Setting up Sprites
P1 = Player()
E1 = Goalkeeper()
B1 = Ball()

# Creating Sprites Groups
# enemies = pygame.sprite.Group()
# enemies.add(E1)
ALL_SPRITES = sprite.Group()
ALL_SPRITES.add(P1, E1, B1)
BALL_GROUP = sprite.Group()
BALL_GROUP.add(B1)
# all_sprites.add(E1)


# Beginning Game Loop
while True:
    display.update()
    for ev in event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()

    if sprite.spritecollide(P1, BALL_GROUP, False):
        print("Test successful")

    DISPLAYSURF.blit(BACKGROUND, (0, 0))

# Moves and Re-draws all Sprites
    for entity in ALL_SPRITES:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.update()
