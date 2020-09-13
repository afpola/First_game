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
from utility import load_image, position_from_center
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, BLACK, BALL_SPEED

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
GOALKEEPER_GROUP = sprite.Group()
GOALKEEPER_GROUP.add(E1)
# all_sprites.add(E1)


# Beginning Game Loop
while True:
    display.update()
    for ev in event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()

    # Sprite collide functions, player ball:

    if sprite.spritecollide(P1, BALL_GROUP, False):

        B1.velocity.x = (B1.rect.centerx - P1.rect.centerx)
        B1.velocity.y = (B1.rect.centery - P1.rect.centery)

        B1.velocity = B1.velocity.normalize() * BALL_SPEED


# Goal:

    if B1.rect.y < 0:
        B1.velocity = pygame.Vector2(0, 0)

        P1.reset()

        position_from_center(B1.rect, 0, 0)

        # B1.rect = B1.surf.get_rect(
        #     center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        print("Goal")

# Wall collisons:

    if B1.rect.y > SCREEN_HEIGHT:
        B1.velocity = B1.velocity.reflect(pygame.math.Vector2(0, 1))

    if B1.rect.x > SCREEN_WIDTH:
        B1.velocity = B1.velocity.reflect(pygame.math.Vector2(1, 0))

    if B1.rect.x < 0:
        B1.velocity = B1.velocity.reflect(pygame.math.Vector2(1, 0))

# Goalkeeper collision:

    if sprite.spritecollide(E1, BALL_GROUP, False):

        B1.velocity.x = (B1.rect.centerx - E1.rect.centerx)
        B1.velocity.y = (B1.rect.centery - E1.rect.centery)

        B1.velocity = B1.velocity.normalize() * BALL_SPEED / 2
        print("Save")

    # Earlier:
    # B1.velocity = B1.velocity.reflect(pygame.math.Vector2(0, 1))

    DISPLAYSURF.blit(BACKGROUND, (0, 0))

# Moves and Re-draws all Sprites
    for entity in ALL_SPRITES:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.update()
