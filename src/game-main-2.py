import pygame
import sys
from pygame.locals import *
from characters import Enemy, Player

# initialization
pygame.init()
FRAME_RATE = 60
fps = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DISPLAY_SURF = pygame.display.set_mode((400, 600))
DISPLAY_SURF.fill(WHITE)
pygame.display.set_caption("The Game")
# draw
p1 = Player()
e1 = Enemy()

while True:
    p1.update()
    e1.move()
    DISPLAY_SURF.fill(WHITE)
    p1.draw(DISPLAY_SURF)
    e1.draw(DISPLAY_SURF)
    fps.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()