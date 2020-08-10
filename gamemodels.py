"""containing all games models
"""
import pygame
from pygame.locals import *  # pylint: disable=wildcard-import, unused-wildcard-import
from utility import load_image
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPEED

# pylint: disable=pointless-string-statement

"""
Creating a class for my player

- Task/new issue(3): Move player class to separate file.
Hmm have to check how the files connect, from earlier projects.
I mean when you run. Maybe you don't have to do anything, maybe vscode recognizes regardless
because it's within the system so to speak.

Min tolkning av svar på stackflow-fråga: Man importerar vid toppen de filer man vill ska hänga ne.
Så i player.py importeras mygame och tvärtom osv. Men som sagt kolla i våra tidigare projekt.
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


"""
H göra funktionen så blir det bra.

"""
