# Example file showing a circle moving on screen
import random
import pygame
from Asteroid import Asteroid
from Player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption('Asteroid')

# asteroid details
asteroid_max_speed = 100
asteroids = []

# read images from disk
asteroid_sprite = pygame.image.load('resources/asteroid.png')
asteroid_sprite = pygame.transform.scale(asteroid_sprite, (100, 100))
player_sprite = pygame.image.load("resources/ship.png")
player_sprite = pygame.transform.scale(player_sprite, (100, 100))
background_sprite = pygame.image.load("resources/background.png")

# Create a player
player = Player(screen, player_sprite, pygame.Vector2(300,300))

# Create asteroids
for i in range(0,1):
    rand_pos = pygame.Vector2(random.randrange(0, screen.get_width()), random.randrange(0, screen.get_height()))
    rand_speed = pygame.Vector2(random.randrange(-asteroid_max_speed, asteroid_max_speed),
                                random.randrange(-asteroid_max_speed, asteroid_max_speed))
    asteroids.append(Asteroid(screen, asteroid_sprite, rand_pos, rand_speed))



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Update things
    keys = pygame.key.get_pressed() # Lets fetch all the keys that are pressed

    player.update(dt, keys)
    for asteroid in asteroids:
        asteroid.update(dt)

    # collision
    for asteroid in asteroids:
        if asteroid.overlaps(player):
            pygame.display.set_caption('Player is hit')


    # draw things
    screen.blit(background_sprite, pygame.Vector2(0,0))     # Lets draw the bakground.
    player.draw()
    for asteroid in asteroids:
        asteroid.draw()


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(144) / 1000

pygame.quit()
