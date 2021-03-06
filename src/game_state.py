import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
CAN_SHOOT = True
POWER = 0
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
BULLETS = [
    {
        "image": pygame.image.load("resources/bullet.png"),
        "dim": (5, 15)
    },
    {
        "image": pygame.image.load("resources/bullet2.png"),
        "dim": (15, 15)
    },
    {
        "image": pygame.image.load("resources/bullet3.png"),
        "dim": (25, 15)
    },
    {
        "image": pygame.image.load("resources/bullet4.png"),
        "dim": (35, 15)
    },
    {
        "image": pygame.image.load("resources/bullet5.png"),
        "dim": (45, 15)
    }
]
LANE_IMG = pygame.image.load("resources/lane.png")
PLAYER_IMG = pygame.image.load("resources/car1.png")
