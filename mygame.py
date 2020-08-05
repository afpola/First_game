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
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 484
SPEED = 5
SCORE = 0

# Setting up Fonts
FONT = pygame.font.SysFont("Verdana", 60)
FONT_SMALL = pygame.font.SysFont("Verdana", 20)
GAME_OVER = FONT.render("Game Over", True, BLACK)


""" TASK Create background & import
This path function is used for saving time and space, not having to type out or paste path
"""


def assets_folder(filename):
    """Returns absolute path to the assets folder

    Args:
        filename (string): the filename

    Returns:
        string: the absolute path
    """
    assets_path = 'C:/Users/46707/Work/firstgame/Import_files'
    return "{}/{}".format(assets_path, filename)


def load_image(filename):
    """loads image from the assets folder

    Args:
        filename (string): the filename

    Returns:
        string: the image object
    """
    return pygame.image.load(assets_folder(filename))


BACKGROUND = load_image("pitch640x484.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

"""
Creating a class for my player

- Task/new issue(3): Move player class to separate file.
Hmm have to check how the files connect, from earlier projects.
I mean when you run. Maybe you don't have to do anything, maybe vscode recognizes regardless
because it's within the system so to speak.

"""


class Player(pygame.sprite.Sprite):
    """Creating a class for my player

    Args:
        pygame ([type]): [description]
    """

    def __init__(self):
        super().__init__()
        self.image = load_image("Player.png")
        self.surf = pygame.Surface((99, 126))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.8))

    def update(self):
        """sssss
        """
        pressed_keys = pygame.key.get_pressed()
       # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
       # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-SPEED, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(SPEED, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -SPEED)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, SPEED)


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
