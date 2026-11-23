import pygame
import random

from const import *


class Ground:

    def __init__(self):
        self.image = pygame.image.load('assets/ground.png')

        self.x = 0
        self.y = SCREEN_HEIGHT - self.image.get_height() - 2

        self.next_cactus = 800
        self.cactus = []

        self.velocity = 8

        self.move = False

    def update(self, window):
        if self.move:
            self.x -= self.velocity
            self.next_cactus -= self.velocity
            if self.next_cactus - self.velocity < 0:
                self.add_cactus()

            for element in self.cactus:
                element[0] -= self.velocity

        window.blit(self.image, (self.x, self.y))

        for element in self.cactus:
            x, image = element
            window.blit(image, (x, SCREEN_HEIGHT-image.get_height()))

        if -self.x + SCREEN_WIDTH > self.image.get_width():
            window.blit(self.image, (self.x + self.image.get_width(), self.y))

        if -self.x > self.image.get_width():
            self.x = 0

    def add_cactus(self):
        self.next_cactus = random.randint(500, 800)
        self.cactus.append([SCREEN_WIDTH, pygame.image.load(f'assets/cactus/cactus_{random.randint(1, 6)}.png')])