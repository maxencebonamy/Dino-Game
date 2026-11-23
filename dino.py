import pygame

from const import *


class Dino:

    def __init__(self, x, y):
        self.images = {
            'before_starting': pygame.image.load('assets/dino/before_starting.png'),
            'jump': pygame.image.load('assets/dino/jump.png'),
            'walk_1': pygame.image.load('assets/dino/walk_1.png'),
            'walk_2': pygame.image.load('assets/dino/walk_2.png'),
            'snick_1': pygame.image.load('assets/dino/snick_1.png'),
            'snick_2': pygame.image.load('assets/dino/snick_2.png'),
        }

        self.image = self.images['before_starting']

        self.x = x
        self.y = SCREEN_HEIGHT - y - self.image.get_height()

        self.dy = 0

        self.step_duration = 10
        self.current_step = 0
        self.step = 1

        self.idle = True
        self.is_walking = False
        self.is_jumping = False
        self.game_over = False

    def update(self, window, keys):
        if not self.game_over:
            moving = 'snick' if keys.get(pygame.K_DOWN) else 'walk'

            if keys.get(pygame.K_SPACE) or keys.get(pygame.K_UP):
                if self.idle:
                    self.start()
                elif moving == 'walk':
                    self.jump()

            # jump
            if self.is_jumping:
                self.dy += 0.55
                self.y += self.dy

                if self.y >= SCREEN_HEIGHT - self.image.get_height():
                    self.y = SCREEN_HEIGHT - self.image.get_height()
                    self.dy = 0
                    self.is_jumping = False
                    self.is_walking = True
                    self.image = self.images[f'{moving}_1']

            # change step
            if self.is_walking:
                self.current_step += 1
                if self.current_step == self.step_duration:
                    self.current_step = 0
                    self.step = 2 if self.step == 1 else 1
                    self.image = self.images[f'{moving}_{self.step}']

        window.blit(self.image, (self.x, self.y))

    def start(self):
        self.idle = False
        self.jump()

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.is_walking = False
            self.image = self.images['jump']
            self.dy = -14