import pygame
import random
from pygame.locals import *
import game_state

class Lane(pygame.sprite.Sprite):
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load("resources/lane.png")
        self.surf = pygame.Surface((20, 40))
        self.rect = self.surf.get_rect(center=(190, y_pos))
    def move(self):
        self.rect.move_ip(0, 5)
        if (self.rect.bottom > game_state.SCREEN_HEIGHT + 40):
            self.rect.top = -40

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/car2.png")
        self.surf = pygame.Surface((68, 100))
        self.rect = self.surf.get_rect(center=(random.randint(40, game_state.SCREEN_WIDTH - 40), 0))
    
    def move(self):
        self.rect.move_ip(0, game_state.SPEED)
        if (self.rect.bottom > game_state.SCREEN_HEIGHT):
            game_state.SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, game_state.SCREEN_WIDTH - 40), 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/car1.png")
        self.surf = pygame.Surface((69, 100))
        self.rect = self.surf.get_rect(center=(160, 500))
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < game_state.SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)