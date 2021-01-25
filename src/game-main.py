import pygame
import sys
from pygame.locals import *

# initialization
pygame.init()
FRAME_RATE = 60
fps = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DISPLAY_SURF = pygame.display.set_mode((400, 300))
DISPLAY_SURF.fill(WHITE)
pygame.display.set_caption("The Game")
# draw
pygame.draw.line(DISPLAY_SURF, BLUE, (150, 130), (130, 170))
pygame.draw.line(DISPLAY_SURF, BLUE, (150, 130), (170, 170))
pygame.draw.line(DISPLAY_SURF, GREEN, (130, 170), (170, 170))
pygame.draw.circle(DISPLAY_SURF, BLACK, (100, 50), 30)
pygame.draw.circle(DISPLAY_SURF, BLACK, (200, 50), 30)
pygame.draw.rect(DISPLAY_SURF, RED, (100, 200, 100, 50), 2)
pygame.draw.rect(DISPLAY_SURF, BLACK, (110, 260, 80, 5))
while True:
    fps.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()