import pygame
from pygame.locals import *
import random

pygame.init()

# constant
SIZE = W, H = 864, 936
FPS = 60
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont("Carito", 60)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SIZE))
pygame.display.set_caption('Flappy Bird')


#define game variables
ground_pos = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks()
score = 0
pass_pipe = False

#load images
bg = pygame.image.load('images/bg.png')
ground_img = pygame.image.load('images/ground.png')

def draw_text(text, font, txt_color, x, y):
	txt_img = font.render(text, True, txt_color)
	screen.blit(txt_img, (x, y))
class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range(1, 4):
			img = pygame.image.load(f'images/bird{num}.png')
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.velocity = 0
		self.tapped = False
	def update(self):

		# gravity
		if flying:		
			self.velocity += 0.5
			if self.velocity > 8:
				self.velocity = 8
			elif self.velocity < -10:
				self.velocity = -10
			if self.rect.bottom < 768:
				self.rect.y += int(self.velocity)


		if not game_over:
			# jump
			if pygame.key.get_pressed()[K_SPACE] == 1 and self.tapped == False:
				self.tapped = True
				self.velocity -= 10
			if pygame.key.get_pressed()[K_SPACE] == 0:
				self.tapped = False
			#handle the animation
			self.counter += 1
			flap_cooldown = 5

			if self.counter > flap_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images):
					self.index = 0
			self.image = self.images[self.index]

			# rotate the bird
			self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -1)
		else:
			self.image = pygame.transform.rotate(self.images[self.index], -82)


class Pipe(pygame.sprite.Sprite):
	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/pipe.png')
		self.rect = self.image.get_rect()
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - pipe_gap // 2]
		elif position == -1:
			self.rect.topleft = [x, y + pipe_gap // 2]
	
	def update(self):
		if not game_over:
			self.rect.x -= scroll_speed
			if self.rect.right < 0:
				self.kill()



pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

flappy = Bird(100, (H // 2))
bird_group.add(flappy)


run = True
while run:

	clock.tick(FPS)

	# draw background
	screen.blit(bg, (0,0))

	bird_group.draw(screen)
	bird_group.update()
	pipe_group.draw(screen)
	pipe_group.update()
	

	# draw the ground
	screen.blit(ground_img, (ground_pos, 768))

	# check points
	if len(pipe_group) > 0:
		if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
		and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and not pass_pipe:
			pass_pipe = True
		if pass_pipe:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
				score += 1
				pass_pipe = False

	draw_text(str(score), FONT, WHITE, W // 2, 20)

	# collisions
	if pygame.sprite.pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
		game_over = True

	# check if bird has hit on the ground
	if flappy.rect.bottom > 768 :
		game_over = True
		flying = False

	
	if not game_over and flying:

	# generate pipes
		time_now = pygame.time.get_ticks()
		if time_now - last_pipe > pipe_frequency:
			pipe_height = random.randint(-100, 100)
			bottom_pipe = Pipe(W, H // 2 + pipe_height, -1)
			top_pipe = Pipe(W, H // 2 + pipe_height, 1)
			pipe_group.add(bottom_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now

	#  scroll the ground
		ground_pos -= scroll_speed
		if abs(ground_pos) > 35:
			ground_pos = 0

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN and not flying and not game_over:
			flying = True
	
	
	pygame.display.update()

pygame.quit()