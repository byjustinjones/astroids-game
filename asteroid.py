import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            self.velocity.rotate(random.uniform(20, 50))
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.new_radius)
            asteroid_1.velocity = self.velocity * 1.2
            asteroid_2.velocity = self.velocity * -1
            asteroid_1.new_radius = self.new_radius
            asteroid_2.new_radius = self.new_radius
            self.kill()
