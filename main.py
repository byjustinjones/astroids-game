import pygame
import constants
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

update_sprites = pygame.sprite.Group()
draw_sprites = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
shot_group = pygame.sprite.Group()

Player.containers = (update_sprites, draw_sprites)
Asteroid.containers = (update_sprites, draw_sprites, asteroid_group)
Shot.containers = (update_sprites, draw_sprites, shot_group)
AsteroidField.containers = (update_sprites,)



def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroids = AsteroidField()

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
        for asteroid in asteroid_group:
            if player.collision(asteroid):
                print("Game Over")
                pygame.quit()
                return
            for shot in shot_group:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
