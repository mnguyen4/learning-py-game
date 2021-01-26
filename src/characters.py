import pygame, sys, random
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/car2.png")
        self.surf = pygame.Surface((68, 100))
        self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH-40), 0))
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/car1.png")
        self.surf = pygame.Surface((69, 100))
        self.rect = self.surf.get_rect(center=(150, 500))
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)