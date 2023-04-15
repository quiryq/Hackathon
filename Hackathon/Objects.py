
from Player import Player
from Base import Base
import pygame, var
Bird = Player(var.skin)
Base = Base()

all_sprites = pygame.sprite.Group()
all_sprites.add(Bird)
trigger = pygame.sprite.Group()