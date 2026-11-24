import pygame
import random

from const import *


class Cloud:

    def __init__(self):
        self.image = pygame.image.load('assets/cloud.png')

        self.clouds = []
        self.next_cloud = 300

        self.velocity = 3

    def update(self, window, move):
        if move:
            self.next_cloud -= self.velocity
            if self.next_cloud < 0:
                self.add_cloud()

            for cloud in self.clouds:
                cloud[0] -= self.velocity

            self.clouds = [cloud for cloud in self.clouds if cloud[0] > -self.image.get_width()]

        for x, y in self.clouds:
            window.blit(self.image, (x, y))

    def add_cloud(self):
        self.next_cloud = random.randint(250, 500)
        self.clouds.append([SCREEN_WIDTH, random.randint(20, 100)])

    def reset(self):
        self.clouds = []
        self.next_cloud = 300
