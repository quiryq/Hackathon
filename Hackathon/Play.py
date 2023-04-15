import pygame, var, Objects, sys
from Functions import *
from Base import Base
from Player import Player

def game():
        Objects.Bird = Player(var.skin)
        Objects.Base = Base()

        Objects.all_sprites = pygame.sprite.Group()
        Objects.all_sprites.add(Objects.Bird)
        Objects.trigger = pygame.sprite.Group()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            
            var.screen.blit(var.background, (0,0))
            for sprite in Objects.all_sprites:
                sprite.move()
            newPipe = getRandomPipe()
            time_now = pygame.time.get_ticks()
            createPipes(newPipe, time_now)
            renderScore()
            crashTest()

            Objects.Base.move()

            pygame.display.update()
            var.fps_clock.tick(var.framePerSecond)