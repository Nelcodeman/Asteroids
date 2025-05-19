import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot
from constants import *
from player import Player


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Shot.containers = (bullets, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update Game state
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

            for bullet in bullets:
                if asteroid.check_collision(bullet):
                    asteroid.split()
                    bullet.kill()

        # Clear screen and draw
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        # Show new frame
        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = (clock.tick(60)) / 1000


if __name__ == "__main__":
    main()
