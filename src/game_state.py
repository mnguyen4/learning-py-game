import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
CAN_SHOOT = True
# user events
INC_SPEED = pygame.USEREVENT + 1
SPAWN_ENEMY = pygame.USEREVENT + 2
SHOOT = pygame.USEREVENT + 3
RELOAD = pygame.USEREVENT + 4
# image cache
ENEMIES = [
    {
        "image": pygame.image.load("resources/car2.png"),
        "dim": (68, 100)
    },
    {
        "image": pygame.image.load("resources/motorcycle.png"),
        "dim": (20, 60)
    },
    {
        "image": pygame.image.load("resources/tractor.png"),
        "dim": (78, 100)
    }
]
BULLET_IMG = pygame.image.load("resources/bullet.png")
