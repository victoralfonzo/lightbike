import pygame

WIDTH = 720
HEIGHT = 400


FPS = 30
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
trails = pygame.sprite.Group()
players = pygame.sprite.Group()
