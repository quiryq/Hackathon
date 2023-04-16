import pygame, var, Objects, sys
from Functions import renderScore
from Functions import winwindow
from Base import Base
from Player import Player
from Pipe import *
from Bullet import Bullet

def game():
        Objects.Bird = Player(var.skin)
        Objects.Base = Base()
        
        Objects.all_sprites = pygame.sprite.Group()
        Objects.all_sprites.add(Objects.Bird)
        Objects.trigger = pygame.sprite.Group()
        pygame.mixer.music.load('music/game_music.mp3')
        pygame.mixer.music.play()

        while True:
            if var.score >= 100:
                winwindow()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if var.secondLevel or var.thirdLevel:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        bullet = Bullet(Objects.Bird.rect.midright[0],Objects.Bird.rect.midright[1], 12 )
                        Objects.all_sprites.add(bullet)
                        Objects.bullet.add(bullet)
                
                    
            var.screen.blit(var.background, (0,0))
            for sprite in Objects.all_sprites:
                sprite.move()
            newPipe = getRandomPipe()
            time_now = pygame.time.get_ticks()
            if var.firstLevel:
                createPipes(newPipe,time_now)
            elif var.secondLevel:
                createEnemies(newPipe,time_now)
            # elif var.thirdLevel:
            #     createMario()

            renderScore()
            crashTest()

            Objects.Base.move()

            pygame.display.update()
            var.fps_clock.tick(var.framePerSecond)