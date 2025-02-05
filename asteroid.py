import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
  def update(self, dt):
    self.position += (self.velocity * dt)
    
  def split(self):
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    if new_radius < ASTEROID_MIN_RADIUS:
      self.kill()
      return
    self.kill()
    
    random_angle = random.uniform(20, 50)
    
    new_vel1 = self.velocity.rotate(random_angle)
    new_vel2 = self.velocity.rotate(-random_angle)

    new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid.velocity = new_vel1 * 1.2
    
    new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid2.velocity = new_vel2 * 1.2
    
