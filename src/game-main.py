import pygame
import sys
from pygame.locals import *

pygame.init()

# main game loop
while True:
    # todo
    DISPLAY_SURF = pygame.display.set_mode((400, 300))
    pygame.draw.circle(DISPLAY_SURF, pygame.Color(200, 200, 0), (200, 50), 30)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()