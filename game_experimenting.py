"""
For using Pygame library and must be added before any other pygame function,
else an initialization error may occur.
"""
import sys
import pygame

from pygame.locals import *  # pylint: disable=wildcard-import, unused-wildcard-import


pygame.init()

# pylint: disable=pointless-string-statement
"""
- Every game that exists has what is called a Game Loop.,
It's merely a concept, not some kind of special syntax or function to be called.
- The Game Loop is where all the game events occur, update and get drawn to the screen.
Once the initial setup and initialization of variables is out of the way,
the Game Loop begins where the program keeps looping over and over until an event
of type QUIT occurs.
- Game Loop begins :
"""


""" Changes in the game are not implemented until the display.update() has been called.
 Since games are constantly changing values, the update function is in the game loop,
 constantly updating.

 EVENT OBJECTS: An "event" occurs when the user performs a specific action, such as
 clicking the mouse or pressing a keyboard button. Pygame records each and every
 event that occurs. Find out which events have happened by calling the
 pygame.event.get() function.
 One of the many attributes (or properties) held by EVENT OBJECTS is TYPE.
 The TYPE attribute tells us what kind of EVENT the OBJECT represents.
"""

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
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Setting up Fonts
FONT = pygame.font.SysFont("Verdana", 60)
FONT_SMALL = pygame.font.SysFont("Verdana", 20)
GAME_OVER = FONT.render("Game Over", True, BLACK)
