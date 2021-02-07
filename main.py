import pygame
import random

class MySprite:
  '''Simple sprite, maybe a snowflake?'''

  def __init__(self, pos, size, colour=(255,255,255)):
    '''Wird für jede neue Schneeflocke aufgerufen
    '''
    self.pos = pos
    self.size = size
    self.colour = colour
    self.fixed = False

    # prepare a pygame surface with a coloured circle
    self.surface = pygame.Surface(
      (self.size, self.size)
    )
    pygame.draw.circle(
      self.surface,
      self.colour,
      (self.size/2, self.size/2), 
      self.size/2
    )
    self.surface = self.surface.convert()

  def draw(self, screen):
    screen.blit(self.surface, self.pos)

  def move(self):
    if self.fixed:
      return
    move_y = random.randint(-1, 4)
    move_x = random.randint(-1, 1)
    x_pos, y_pos = self.pos
    x_pos += move_x
    y_pos += move_y

    if y_pos < 290:
      self.pos = (x_pos, y_pos)
    else:
      self.fixed = True

# Frames per second
FPS = 100

RESOLUTION = (300, 300)

LEFT = 1  # left mouse button
MIDDLE = 2
RIGHT = 3  # ...
WHEELUP = 4
WHEELDOWN = 5

screen = pygame.display.set_mode(RESOLUTION)

pygame.display.set_caption("Let it snow!")
pygame.mouse.set_visible(1)

# frame limiter
clock = pygame.time.Clock()

# Initialize font machine
pygame.font.init()
font_size = 15
font = pygame.font.Font(None, font_size)
font_color = (255, 255, 255)
font_pos = (250, 250)

running = True
font_text = "Hello World!"

sprites = []

# number of snowflakes to create on leftclick
flake_count = 10

# main loop
while running:

  clock.tick(FPS)
  background = pygame.Surface(RESOLUTION)
  background.fill((0, 0, 0, 0))
  background = background.convert_alpha()

  font_surface = font.render(font_text, True, font_color)

  screen.blit(background, (0, 0))
  screen.blit(font_surface, font_pos)

  for sprite in sprites:
    sprite.move()
    sprite.draw(screen)

  # look for events
  for event in pygame.event.get():

      # quit game
      if event.type == pygame.QUIT:
        print("User has quitted!")
        running = False

      if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        print('left mouse button at %s' % str(event.pos))
        font_text = str(event.pos)
        for i in range(flake_count):
          sprites.append(MySprite(event.pos, 5))

      if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
        print('right mouse button at %s' % str(event.pos))

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          print("UP key pressed!")

        if event.key == pygame.K_DOWN:
          print("DOWN key pressed!")

  pygame.display.flip()