import pygame
import random

from const import *


class Ground:

    def __init__(self):
        self.image = pygame.image.load('assets/ground.png')

        self.x = 0
        self.y = SCREEN_HEIGHT - self.image.get_height() - 2

        self.cactus_images = [pygame.image.load(f'assets/cactus/cactus_{i}.png') for i in range(1, 7)]
        bird_image = pygame.image.load('assets/bird.png')
        self.bird_frames = [
            bird_image.subsurface((0, 0, 92, 80)),
            bird_image.subsurface((92, 0, 92, 80)),
        ]

        self.next_obstacle = 800
        self.obstacles = []

        self.velocity = 8

        self.move = False

    def update(self, window, score=0):
        if self.move:
            self.velocity = 8 + min(6, score // 150)

            self.x -= self.velocity
            self.next_obstacle -= self.velocity
            if self.next_obstacle - self.velocity < 0:
                self.add_obstacle()

            for obstacle in self.obstacles:
                obstacle['x'] -= self.velocity
                if obstacle['type'] == 'bird':
                    obstacle['timer'] += 1
                    if obstacle['timer'] >= 10:
                        obstacle['timer'] = 0
                        obstacle['frame'] = 1 - obstacle['frame']

            self.obstacles = [obstacle for obstacle in self.obstacles if obstacle['x'] > -200]

        window.blit(self.image, (self.x, self.y))

        for obstacle in self.obstacles:
            image = self.bird_frames[obstacle['frame']] if obstacle['type'] == 'bird' else obstacle['image']
            window.blit(image, (obstacle['x'], obstacle['y']))

        if -self.x + SCREEN_WIDTH > self.image.get_width():
            window.blit(self.image, (self.x + self.image.get_width(), self.y))

        if -self.x > self.image.get_width():
            self.x = 0

    def add_obstacle(self):
        self.next_obstacle = random.randint(500, 800)

        if random.random() < 0.25:
            self.obstacles.append({
                'type': 'bird',
                'x': SCREEN_WIDTH,
                'y': self.y - 80,
                'frame': 0,
                'timer': 0,
            })
        else:
            image = random.choice(self.cactus_images)
            self.obstacles.append({
                'type': 'cactus',
                'x': SCREEN_WIDTH,
                'y': SCREEN_HEIGHT - image.get_height(),
                'image': image,
            })

    def reset(self):
        self.x = 0
        self.next_obstacle = 800
        self.obstacles = []
        self.velocity = 8
        self.move = False
