import pygame
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN 

from circleshape import CircleShape
from constants import PLAYER_RADIUS
from shot import Shot
class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.shoot_timer = 0
    self.score = 0
    self.speed = PLAYER_SPEED

  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)
  
  # in the player class
  def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]

  def rotate(self, dt):
     self.rotation += PLAYER_TURN_SPEED * dt

  def update(self, dt):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
      self.rotate((-1)*dt)
    if keys[pygame.K_d]:
      self.rotate(dt)
    if keys[pygame.K_s]:
      self.move((-1)*dt)
    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_SPACE]:
      self.shoot()
    self.shoot_timer -= dt

  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * self.speed * dt
    if (self.speed < 2000):
      self.speed *= 1.03
  
  def shoot(self):
    if self.shoot_timer > 0:
      return
    velocity = pygame.Vector2(0, 1).rotate(self.rotation)
    Shot(self.position.x, self.position.y, velocity)
    self.shoot_timer = PLAYER_SHOOT_COOLDOWN
    
  def add_score(self):
    self.score += 1
    
  def reset_speed(self):
    self.speed = PLAYER_SPEED