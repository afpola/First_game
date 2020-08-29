"""utility functions
"""
import pygame
from pygame.locals import *  # pylint: disable=wildcard-import, unused-wildcard-import
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


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


def position_from_center(rect, pos_x, pos_y):
    """Position a rect offset from center with pos x, pos y.

    """
    rect.x = ((SCREEN_WIDTH / 2) - (rect.width / 2)) + pos_x
    rect.y = ((SCREEN_HEIGHT / 2) - (rect.height / 2)) + pos_y
