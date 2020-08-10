"""utility functions
"""
import pygame
from pygame.locals import *  # pylint: disable=wildcard-import, unused-wildcard-import


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
