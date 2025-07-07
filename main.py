import pygame
import constants
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

update_sprites = pygame.sprite.Group()
draw_sprites = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()

# Set containers for Player and Asteroid classes
Player.containers = (update_sprites, draw_sprites)
Asteroid.containers = (update_sprites, draw_sprites, asteroid_group)

# Set containers for AsteroidField
AsteroidField.containers = (update_sprites,)



def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Create AsteroidField instance
    asteroids = AsteroidField()
    
    # Create Player instance
    player = Player(
        constants.SCREEN_WIDTH // 2,
        constants.SCREEN_HEIGHT // 2,
        constants.PLAYER_RADIUS,
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for sprite in draw_sprites:
            sprite.draw(screen)
        update_sprites.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
