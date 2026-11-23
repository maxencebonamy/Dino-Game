import pygame

from const import *
from dino import Dino
from ground import Ground


class Game:

    def __init__(self):
        self.ingame = False
        self.game_over = False

        self.dino = Dino(96, 0)
        self.ground = Ground()

    def update(self, window, keys):
        if (keys.get(pygame.K_SPACE) or keys.get(pygame.K_UP)) and not self.ingame:
            self.start()

        self.dino.update(window, keys)

        if self.ingame and not self.dino.is_jumping and not self.ground.move and not self.game_over:
            self.ground.move = True

        if self.ingame:
            self.ground.update(window)

        for cactus in self.ground.cactus:
            x, image = cactus
            dino = self.dino.image
            if pygame.Rect(x, SCREEN_HEIGHT - image.get_height(), *image.get_size()).colliderect(
                pygame.Rect(self.dino.x, self.dino.y, *dino.get_size())
            ):
                self.game_over = True
                self.ground.move = False
                self.dino.game_over = True

    def start(self):
        self.ingame = True
        self.dino.start()