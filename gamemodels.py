"""containing all games models
"""
import pygame
from pygame.locals import *  # pylint: disable=wildcard-import, unused-wildcard-import
from utility import load_image, position_from_center
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPEED, GOALKEEPER_SPEED  # , RED
#from mygame import DISPLAYSURF
# pylint: disable=pointless-string-statement

"""
Creating a class for my player


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
        self.rect = self.surf.get_rect()
        self.reset()

    def reset(self):
        """fix descript later
        """
        position_from_center(self.rect, 0, 150)

    def update(self):
        """fix descript later
        """
        player_movement = pygame.math.Vector2()

        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            player_movement.x = player_movement.x - SPEED
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            player_movement.x = player_movement.x + SPEED
        if self.rect.top > 0 and pressed_keys[K_UP]:
            player_movement.y = player_movement.y - SPEED
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            player_movement.y = player_movement.y + SPEED

        if player_movement.length() > 0:
            player_movement = player_movement.normalize() * SPEED
            self.rect.move_ip(player_movement.x, player_movement.y)


class Goalkeeper(pygame.sprite.Sprite):
    """Creating a class for enemy/goalkeeper

    Args:
        pygame ([type]): [description]
    """

    def __init__(self):
        super().__init__()
        self.image = load_image("Enemy.png")
        self.surf = pygame.Surface((99, 126))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.2))
        self.velocity = pygame.math.Vector2(GOALKEEPER_SPEED, 0)

    def update(self):
        """sssss
        """
        self.rect.move_ip(self.velocity.x, self.velocity.y)

        if self.rect.x > SCREEN_WIDTH * 0.85 or self.rect.x < 0:
         #   self.velocity = self.velocity.reflect(-self.velocity)
            self.velocity = -self.velocity


class Ball(pygame.sprite.Sprite):
    """Creating a class for ball
    """

    def __init__(self):
        super().__init__()
        self.image = load_image("Ball.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        """Move the ball sprite with the balls current velocity.
        """
        self.rect.move_ip(self.velocity.x, self.velocity.y)

# Add function to make ball speed decrease by time
