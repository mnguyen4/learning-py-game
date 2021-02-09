import game_state
import sys
from pygame.locals import *
from characters import *

def title(game_surface, background):
    fps = pygame.time.Clock()
    game_surface.blit(background, (0, 0))
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
    resume_btn = Button(game_state.RESUME_IMG, game_state.SCREEN_HEIGHT / 2)
    game_surface.blit(resume_btn.image, resume_btn.rect)
    quit_btn = Button(game_state.QUIT_IMG, game_state.SCREEN_HEIGHT / 2 + 50)
    game_surface.blit(quit_btn.image, quit_btn.rect)
    while game_state.MENU:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state.MENU = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_btn.rect.left <= mouse[0] <= resume_btn.rect.right and resume_btn.rect.top <= mouse[1] <= resume_btn.rect.bottom:
                    game_state.MENU = False
                if quit_btn.rect.left <= mouse[0] <= quit_btn.rect.right and quit_btn.rect.top <= mouse[1] <= quit_btn.rect.bottom:
                    pygame.event.post(pygame.event.Event(QUIT))
        fps.tick(game_state.FRAME_RATE)
        pygame.display.update()
