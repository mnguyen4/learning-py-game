import game_state
import sys
from pygame.locals import *
from characters import *

def menu(game_surface):
    fps = pygame.time.Clock()
    font = pygame.font.SysFont("Verdana", 40)
    small_font = pygame.font.SysFont("Verdana", 20)
    menu_txt = font.render("Menu", True, game_state.WHITE)
    resume_txt = small_font.render("Resume", True, game_state.BLACK)
    quit_txt = small_font.render("Quit", True, game_state.BLACK)
    game_surface.fill(game_state.BLACK)
    game_surface.blit(menu_txt, (game_state.SCREEN_WIDTH / 2 - menu_txt.get_width() / 2, game_state.SCREEN_HEIGHT / 3))
    resume_btn = Button(resume_txt, game_state.GREEN)
    resume_btn.rect = resume_btn.surf.get_rect(center=(game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT / 2))
    game_surface.blit(resume_btn.surf, resume_btn.rect)
    quit_btn = Button(quit_txt, game_state.RED)
    quit_btn.rect = quit_btn.surf.get_rect(center=(game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT / 2 + 50))
    game_surface.blit(quit_btn.surf, quit_btn.rect)
    while game_state.MENU:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_btn.rect.left <= mouse[0] <= resume_btn.rect.right and resume_btn.rect.top <= mouse[1] <= resume_btn.rect.bottom:
                    game_state.MENU = False
                if quit_btn.rect.left <= mouse[0] <= quit_btn.rect.right and quit_btn.rect.top <= mouse[1] <= quit_btn.rect.bottom:
                    pygame.quit()
                    sys.exit()
        fps.tick(game_state.FRAME_RATE)
        pygame.display.update()
