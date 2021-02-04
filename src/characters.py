import pygame
import random
from pygame.locals import *
import game_state

class Lane(pygame.sprite.Sprite):
    def __init__(self, y_pos):
        super().__init__()
        self.image = game_state.LANE_IMG
        self.surf = pygame.Surface((20, 40))
        self.rect = self.surf.get_rect(center=(game_state.SCREEN_WIDTH / 2, y_pos))
    def move(self):
        self.rect.move_ip(0, 5)
        if (self.rect.bottom > game_state.SCREEN_HEIGHT + 20):
            self.rect.top = -20

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.image = enemy["image"]
        self.surf = pygame.Surface(enemy["dim"])
        self.rect = self.surf.get_rect(center=(random.randint(40, game_state.SCREEN_WIDTH - 40), self.surf.get_height() * -1))
    
    def move(self):
        self.rect.move_ip(0, game_state.SPEED)
        if (self.rect.bottom > game_state.SCREEN_HEIGHT + self.surf.get_height()):
            game_state.SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, game_state.SCREEN_WIDTH - 40), self.surf.get_height() * -1)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game_state.PLAYER_IMG
        self.surf = pygame.Surface((69, 100))
        self.rect = self.surf.get_rect(center=(game_state.SCREEN_WIDTH / 2, game_state.SCREEN_HEIGHT - 60))
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < game_state.SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if pressed_keys[K_SPACE]:
            if game_state.CAN_SHOOT:
                game_state.CAN_SHOOT = False
                pygame.time.set_timer(game_state.RELOAD, 1000)
                pygame.event.post(pygame.event.Event(game_state.SHOOT))

    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = game_state.BULLETS[game_state.POWER]["image"]
        self.surf = pygame.Surface(game_state.BULLETS[game_state.POWER]["dim"])
        self.rect = self.surf.get_rect(center=pos)
    
    def move(self):
        self.rect.move_ip(0, -5)
        if (self.rect.top < 0):
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
