import pygame
import pygame.freetype
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,ASTEROID_MIN_RADIUS,ASTEROID_KINDS,ASTEROID_SPAWN_RATE,ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
  shots = pygame.sprite.Group()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  my_font = pygame.freetype.SysFont('Ponderosa', 30)

  Asteroid.containers = (asteroids, updatable, drawable)
  Player.containers = (updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)
  
  AsteroidField()
  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

  while (True):
    text_surface = my_font.render(str(player.score), (255,255,255), (0,0,0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        print(player.score)
        return
      if event.type == pygame.KEYUP:
        player.reset_speed()
      
    updatable.update(dt)
    for item in asteroids:
      if item.check_collision(player):
        print(f"score: {player.score}")
        print('Game over!')
        return
    for asteroid in asteroids:
      for shot in shots:
        if shot.check_collision(asteroid):
          player.add_score()
          asteroid.split()
          shot.kill()

    screen.fill("#000000")
    
    for item in drawable:
      item.draw(screen)

    screen.blit(text_surface[0], (SCREEN_WIDTH/2, 50))
    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()