import pygame, var
from Functions import *


def addScore(upperPipes):
    playerMidPos = Objects.Bird.playerX + Objects.Bird.image.get_width()
    pipeMidPos = upperPipes + Objects.Bird.image.get_width()
    if pipeMidPos <= playerMidPos < pipeMidPos + 4:
        pygame.mixer.music.load('music/point.mp3')
        pygame.mixer.music.play()
        var.score += 0.5


class Pipe(pygame.sprite.Sprite):   
    def __init__(self, y_top, y_bottom, angle):
        super().__init__()
        self.image = (
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/textures/pipe.png'), (var.pipeWidth, var.pipeHeight)), 180),
        pygame.transform.scale(pygame.image.load('images/textures/pipe.png'), (var.pipeWidth,  var.pipeHeight))
        )
        self.y_top = y_top
        self.y_bottom = y_bottom
        self.angle = angle
        self.upperPipes = [
            {'x': var.screenWidth + 200, 'y': y_top}
        ]
        self.lowerPipes = [
            {'x': var.screenWidth + 200, 'y': y_bottom}
        ]
        if angle:
            self.rect = self.image[0].get_rect(topleft = (self.upperPipes[0]['x'],self.upperPipes[0]['y'] ) )
        elif not angle:
            self.rect = self.image[1].get_rect(topleft = (self.lowerPipes[0]['x'],self.lowerPipes[0]['y'] ))


    def move(self):
        global score
        self.rect.move_ip(-var.scrollSpeed, 0)
        if self.angle:
            var.screen.blit(self.image[0], self.rect)
        elif not self.angle:
            var.screen.blit(self.image[1], self.rect)
        addScore(self.rect.topleft[0])

        if self.rect.left < -self.image[1].get_width():
            self.kill()