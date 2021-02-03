import pygame
import sys
import time
from pygame.locals import *
from characters import *
import game_state

# initialization
pygame.init()
FRAME_RATE = 60
fps = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# setting font
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over!", True, BLACK)

background = pygame.image.load("resources/background.png")
# create display surface
DISPLAY_SURF = pygame.display.set_mode((game_state.SCREEN_WIDTH, game_state.SCREEN_HEIGHT))
DISPLAY_SURF.fill(WHITE)
pygame.display.set_caption("The Game")
# draw
p1 = Player()
e1 = Enemy(game_state.ENEMIES[random.randint(0, 2)])
lane1 = Lane(y_pos=0)
lane2 = Lane(y_pos=160)
lane3 = Lane(y_pos=320)
lane4 = Lane(y_pos=480)
# sprite group
enemies = pygame.sprite.Group()
enemies.add(e1)
lanes = pygame.sprite.Group()
lanes.add(lane1)
lanes.add(lane2)
lanes.add(lane3)
lanes.add(lane4)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
bullets = pygame.sprite.Group()
pygame.time.set_timer(game_state.INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == game_state.INC_SPEED:
            game_state.SPEED += 0.1
        if event.type == game_state.SPAWN_ENEMY:
            e2 = Enemy(game_state.ENEMIES[random.randint(0, 2)])
            enemies.add(e2)
            all_sprites.add(e2)
        if event.type == game_state.SHOOT:
            bullet = Bullet((p1.rect.centerx, p1.rect.top))
            all_sprites.add(bullet)
            bullets.add(bullet)
        if event.type == game_state.RELOAD:
            game_state.CAN_SHOOT = True
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # display background
    DISPLAY_SURF.blit(background, (0,0))
    # move and redraw
    for lane in lanes:
        DISPLAY_SURF.blit(lane.image, lane.rect)
        lane.move()
    for entity in all_sprites:
        DISPLAY_SURF.blit(entity.image, entity.rect)
        entity.move()
    # display score
    scores = font_small.render("Score: " + str(game_state.SCORE), True, BLUE)
    DISPLAY_SURF.blit(scores, (170,10))
    # collision detection
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound("resources/pop.wav").play()
        DISPLAY_SURF.fill(RED)
        DISPLAY_SURF.blit(game_over, (40, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
    if pygame.sprite.groupcollide(bullets, enemies, True, True):
        pygame.event.post(pygame.event.Event(game_state.SPAWN_ENEMY))
        game_state.SCORE += 10

    fps.tick(60)
    pygame.display.update()
