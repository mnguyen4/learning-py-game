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
ENEMIES = [
    {
        "path": "resources/car2.png",
        "dim": (68, 100)
    },
    {
        "path": "resources/motorcycle.png",
        "dim": (20, 60)
    }
]
