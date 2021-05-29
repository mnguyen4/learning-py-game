import game_state
import sys
from pygame.locals import *
from characters import *

def title(game_surface):
    fps = pygame.time.Clock()
    game_surface.blit(game_state.BG_IMG, (0, 0))
    title_img = Title()
    game_surface.blit(title_img.image, title_img.rect)
    small_font = pygame.font.SysFont("Verdana", 20)
    message_txt = small_font.render("Press any key to start", True, game_state.BLACK)
    game_surface.blit(message_txt, message_txt.get_rect(center=(game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT / 2)))
    display_title = True
    while display_title:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                display_title = False
        fps.tick(game_state.FRAME_RATE)
        pygame.display.update()

def menu(game_surface):
    fps = pygame.time.Clock()
    font = pygame.font.SysFont("Verdana", 40)
    menu_txt = font.render("Menu", True, game_state.WHITE)
    game_surface.fill(game_state.BLACK)
    game_surface.blit(menu_txt, menu_txt.get_rect(center=(game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT / 3)))
    resume_btn = Button(game_state.RESUME_IMG, game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT / 2)
    game_surface.blit(resume_btn.image, resume_btn.rect)
    quit_btn = Button(game_state.QUIT_IMG, game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT / 2 + 50)
    game_surface.blit(quit_btn.image, quit_btn.rect)
    while game_state.MENU:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state.MENU = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if resume_btn.rect.left <= mouse[0] <= resume_btn.rect.right and resume_btn.rect.top <= mouse[1] <= resume_btn.rect.bottom:
                    game_state.MENU = False
                if quit_btn.rect.left <= mouse[0] <= quit_btn.rect.right and quit_btn.rect.top <= mouse[1] <= quit_btn.rect.bottom:
                    pygame.event.post(pygame.event.Event(QUIT))
        fps.tick(game_state.FRAME_RATE)
        pygame.display.update()

def upgrade_menu(game_surface):
    fps = pygame.time.Clock()
    font = pygame.font.SysFont("Verdana", 40)
    font_small = pygame.font.SysFont("Verdana", 15)
    upgrade_txt = font.render("Upgrades", True, game_state.WHITE)
    power_btn = Button(game_state.POWER_IMG, game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT / 4)
    rate_btn = Button(game_state.RATE_IMG, game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT / 4 * 2)
    speed_btn = Button(game_state.SPEED_IMG, game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT / 4 * 3)
    resume_btn = Button(game_state.RESUME_IMG, game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT - 40)
    while game_state.UPGRADE_MENU:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state.UPGRADE_MENU = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if resume_btn.rect.left <= mouse[0] <= resume_btn.rect.right and resume_btn.rect.top <= mouse[1] <= resume_btn.rect.bottom:
                    game_state.UPGRADE_MENU = False
                if game_state.UPGRADE_PTS > 0:
                    if game_state.BULLET_POWER < 4:
                        if power_btn.rect.left <= mouse[0] <= power_btn.rect.right and power_btn.rect.top <= mouse[1] <= power_btn.rect.bottom:
                            game_state.UPGRADE_PTS -= 1
                            game_state.BULLET_POWER += 1
                    if game_state.BULLET_RATE < 20:
                        if rate_btn.rect.left <= mouse[0] <= rate_btn.rect.right and rate_btn.rect.top <= mouse[1] <= rate_btn.rect.bottom:
                            game_state.UPGRADE_PTS -= 1
                            game_state.BULLET_RATE += 1
                    if game_state.BULLET_SPEED < 30:
                        if speed_btn.rect.left <= mouse[0] <= speed_btn.rect.right and speed_btn.rect.top <= mouse[1] <= speed_btn.rect.bottom:
                            game_state.UPGRADE_PTS -= 1
                            game_state.BULLET_SPEED += 1
        upgrade_pts = font_small.render("Upgrade Points: " + str(game_state.UPGRADE_PTS), True, game_state.WHITE)
        game_surface.fill(game_state.BLACK)
        game_surface.blit(power_btn.image, power_btn.rect)
        game_surface.blit(rate_btn.image, rate_btn.rect)
        game_surface.blit(speed_btn.image, speed_btn.rect)
        game_surface.blit(resume_btn.image, resume_btn.rect)
        game_surface.blit(upgrade_txt, upgrade_txt.get_rect(center=(game_state.SCREEN_WIDTH / 2, 40)))
        game_surface.blit(upgrade_pts, upgrade_pts.get_rect(center=(game_state.SCREEN_WIDTH / 2, upgrade_txt.get_rect().bottom + 30)))
        fps.tick(game_state.FRAME_RATE)
        pygame.display.update()

def inc_upgrade():
    if game_state.SCORE >= game_state.UPGRADE_SCORE:
        game_state.UPGRADE_PTS += 1
        game_state.UPGRADE_SCORE += 100

def draw_hud(game_surface):
    # display score
    font_small = pygame.font.SysFont("Verdana", 20)
    scores = font_small.render("Score: " + str(game_state.SCORE), True, game_state.BLUE)
    game_surface.blit(scores, scores.get_rect(center=(game_state.SCREEN_WIDTH / 2, 10)))
    # display menu button
    menu_btn = Button(game_state.MENU_IMG, 40, 20)
    game_surface.blit(menu_btn.image, menu_btn.rect)
    # display upgrade button
    upgrade_btn = Button(game_state.UPGRADE_IMG, game_state.SCREEN_WIDTH - 40, 20)
    game_surface.blit(upgrade_btn.image, upgrade_btn.rect)
