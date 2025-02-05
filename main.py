import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,ASTEROID_MIN_RADIUS,ASTEROID_KINDS,ASTEROID_SPAWN_RATE,ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0

  print('Starting asteroids!')
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  Asteroid.containers = (asteroids, updatable, drawable)
  Player.containers = (updatable, drawable)
  AsteroidField.containers = (updatable)
  
  AsteroidField()
  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

  while (True):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    updatable.update(dt)
    for item in asteroids:
      if item.check_collision(player):
        print('Game over!')
        return

    screen.fill("#000000")
    
    for item in drawable:
      item.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()