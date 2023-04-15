import pygame
# Screen set
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Velocity
framePerSecond = 30
scrollSpeed = 6
fps_clock = pygame.time.Clock()

# Pipes set
pipe_frequency = 1500
pipeGap = screenHeight / 4-45
baseY = screenHeight * 0.75
pipeHeight = 500
pipeWidth = 70
last_pipe = pygame.time.get_ticks()


score = 0


# Skins
skin = pygame.transform.scale(pygame.image.load('images/bird.png'), (50, 50))
firstSkin = pygame.transform.scale(pygame.image.load('images/bird.png'), (50, 50))
skin1 = pygame.transform.scale(pygame.image.load('images/Skins/skin1.png'), (50, 50))
skin2 = pygame.transform.scale(pygame.image.load('images/Skins/skin2.png'), (50, 50))
skin3 = pygame.transform.scale(pygame.image.load('images/Skins/skin3.png'), (50, 50))
skin4 = pygame.transform.scale(pygame.image.load('images/Skins/skin4.png'), (50, 50))

# images
background = pygame.transform.scale(pygame.image.load(r'images/textures/bg.png'), (screenWidth, screenHeight))
gameOver = pygame.transform.scale(pygame.image.load('images/tittles/gameOver.png'), (400, 100))
board = pygame.image.load('images/tittles/board.png')

