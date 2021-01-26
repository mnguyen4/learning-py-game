import pygame
import sys
import time
from pygame.locals import *
from characters import *

# initialization
pygame.init()
FRAME_RATE = 60
fps = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#SCREEN_WIDTH, SCREEN_HEIGHT = getDimension()
DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY_SURF.fill(WHITE)
pygame.display.set_caption("The Game")
# draw
p1 = Player()
e1 = Enemy()
# sprite group
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
# user event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    DISPLAY_SURF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            print("Speed: ", SPEED)
            SPEED += 5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # move and redraw
    for entity in all_sprites:
        DISPLAY_SURF.blit(entity.image, entity.rect)
        entity.move()
    # collision detection
    if pygame.sprite.spritecollideany(p1, enemies):
        DISPLAY_SURF.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)

    fps.tick(60)
    pygame.display.update()