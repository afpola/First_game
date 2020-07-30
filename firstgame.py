""" This is fun """
import pygame

# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of each snake segment
SEGMENT_WIDTH = 15
SEGMENT_HEIGHT = 15
# Margin between each segment
SEGMENT_MARGIN = 3

# Set initial speed
X_CHANGE = SEGMENT_WIDTH + SEGMENT_MARGIN
Y_CHANGE = 0

# blablla


class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function

    # (uppgift hitta varför blå streck, pylint(invalid-name) snake_case)
    # Lösning: Variabelnamnet var för kort.
    # "...a variable name should be descriptive and not too short."
    # Så jag la till 2 x och 2 y på raderna 30 samt 40-41,
    # ska kolla om jag kan hitta bättre namn sen.

    def __init__(self, xxx, yyy):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([SEGMENT_WIDTH, SEGMENT_HEIGHT])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = xxx
        self.rect.y = yyy


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
SCREEN = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Snake Example')

ALLSPRITESLIST = pygame.sprite.Group()

# Create an initial snake
SNAKE_SEGMENTS = []
for i in range(15):
    X = 250 - (SEGMENT_WIDTH + SEGMENT_MARGIN) * i
    Y = 30
    SEGMENT = Segment(X, Y)
    SNAKE_SEGMENTS.append(SEGMENT)
    ALLSPRITESLIST.add(SEGMENT)


CLOCK = pygame.time.Clock()
DONE = False

while not DONE:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True

        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_CHANGE = (SEGMENT_WIDTH + SEGMENT_MARGIN) * -1
                Y_CHANGE = 0
            if event.key == pygame.K_RIGHT:
                X_CHANGE = (SEGMENT_WIDTH + SEGMENT_MARGIN)
                Y_CHANGE = 0
            if event.key == pygame.K_UP:
                X_CHANGE = 0
                Y_CHANGE = (SEGMENT_HEIGHT + SEGMENT_MARGIN) * -1
            if event.key == pygame.K_DOWN:
                X_CHANGE = 0
                Y_CHANGE = (SEGMENT_HEIGHT + SEGMENT_MARGIN)

    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    OLD_SEGMENT = SNAKE_SEGMENTS.pop()
    ALLSPRITESLIST.remove(OLD_SEGMENT)

    # Figure out where new segment will be
    X = SNAKE_SEGMENTS[0].rect.x + X_CHANGE
    Y = SNAKE_SEGMENTS[0].rect.y + Y_CHANGE
    SEGMENT = Segment(X, Y)

    # Insert new segment into the list
    SNAKE_SEGMENTS.insert(0, SEGMENT)
    ALLSPRITESLIST.add(SEGMENT)

    # -- Draw everything
    # Clear screen
    SCREEN.fill(BLACK)

    ALLSPRITESLIST.draw(SCREEN)

    # Flip screen
    pygame.display.flip()

    # Pause
    CLOCK.tick(5)

pygame.quit()
