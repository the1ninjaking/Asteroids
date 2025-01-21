# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for update in updatable:
            update.update(dt)
        for asteroid in asteroids:
             for shot in shots:
                 if shot.is_colliding(asteroid):
                     shot.kill()
                     asteroid.kill()
             if player.is_colliding(asteroid):
                 print("Game over!")
                 sys.exit()
        screen.fill(000)  # screen background rendered
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()  # screen is updated
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()