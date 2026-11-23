import pygame

from const import *
from game import Game

pygame.init()

window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Dino Game')

game = Game()

keys = {}


run = True

while run:
    window.fill(SCREEN_COLOR)

    game.update(window, keys)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            keys[event.key] = True
        elif event.type == pygame.KEYUP:
            keys[event.key] = False

    pygame.time.wait(1000 // SCREEN_FPS)