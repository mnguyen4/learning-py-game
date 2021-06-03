import pygame
import sys
import time
import math
from pygame.locals import *
from characters import *
import game_state
import game_functions

# initialization
pygame.init()
fps = pygame.time.Clock()
game_state.RELOAD = game_state.FRAME_RATE
game_state.TIMER = game_state.RELOAD
# setting font
font_small = pygame.font.SysFont("Verdana", 20)
game_over = GameOver()
# create display surface
DISPLAY_SURF = pygame.display.set_mode((game_state.SCREEN_WIDTH, game_state.SCREEN_HEIGHT))
DISPLAY_SURF.fill(game_state.WHITE)
pygame.display.set_caption("The Game")
game_functions.title(DISPLAY_SURF)
# draw
p1 = Player()
e1 = Enemy(game_state.ENEMIES[random.randint(0, 2)])
# sprite group
enemies = pygame.sprite.Group()
enemies.add(e1)
lanes = pygame.sprite.Group()
Y_SPACING = game_state.SCREEN_HEIGHT / 4
for i in range(4):
    lane = Lane(y_pos=Y_SPACING * i)
    lanes.add(lane)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
bullets = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 0 <= mouse[0] <= 80 and 0 <= mouse[1] <= 40:
                game_state.MENU = True
                game_functions.menu(DISPLAY_SURF)
            if game_state.SCREEN_WIDTH - 80 <= mouse[0] <= game_state.SCREEN_WIDTH and 0 <= mouse[1] <= 40 and game_state.UPGRADE_PTS > 0:
                game_state.UPGRADE_MENU = True
                game_functions.upgrade_menu(DISPLAY_SURF)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state.MENU = True
                game_functions.menu(DISPLAY_SURF)
            if event.key == pygame.K_u and game_state.UPGRADE_PTS > 0:
                game_state.UPGRADE_MENU = True
                game_functions.upgrade_menu(DISPLAY_SURF)
        if event.type == game_state.SPAWN_ENEMY:
            e2 = Enemy(game_state.ENEMIES[random.randint(0, 2)])
            enemies.add(e2)
            all_sprites.add(e2)
        if event.type == game_state.SHOOT:
            if game_state.TIMER >= game_state.RELOAD:
                game_state.TIMER = 0
                game_state.FIRED = 0
            if game_state.FIRED < game_state.BULLET_RATE:
                bullet = Bullet((p1.rect.centerx, p1.rect.top))
                all_sprites.add(bullet)
                bullets.add(bullet)
                game_state.FIRED += 1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # display background
    DISPLAY_SURF.blit(game_state.BG_IMG, (0,0))
    # move and redraw
    for lane in lanes:
        DISPLAY_SURF.blit(lane.image, lane.rect)
        lane.move()
    for entity in all_sprites:
        DISPLAY_SURF.blit(entity.image, entity.rect)
        entity.move()
    game_functions.draw_hud(DISPLAY_SURF)
    game_functions.inc_upgrade()
    # scale speed on kill count
    game_state.SPEED = math.log(game_state.KILL_CNT, 6) if game_state.KILL_CNT > 0 else 0
    # collision detection
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound("resources/pop.wav").play()
        DISPLAY_SURF.fill(game_state.RED)
        DISPLAY_SURF.blit(game_over.image, game_over.rect)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
    for bullet in bullets:
        enemy = pygame.sprite.spritecollideany(bullet, enemies)
        if enemy:
            if enemy.hit_points - (game_state.BULLET_POWER + 1) > 0:
                enemy.hit_points -= (game_state.BULLET_POWER + 1)
                bullet.kill()
            else:
                game_state.SCORE += enemy.base_score + round(game_state.SPEED)
                enemy.kill()
                game_state.KILL_CNT += 1
                bullet.kill()
                pygame.event.post(pygame.event.Event(game_state.SPAWN_ENEMY))
            

    fps.tick(game_state.FRAME_RATE)
    if game_state.TIMER < game_state.RELOAD:
        game_state.TIMER += 1
    pygame.display.update()
