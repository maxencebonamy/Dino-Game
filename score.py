import pygame

from const import *


CHARS = '0123456789HI'
RECTS = [
    (0, 18), (22, 16), (40, 18), (60, 18), (80, 18), (100, 18),
    (120, 18), (140, 18), (160, 18), (180, 18), (200, 18), (222, 16),
]


class Score:

    def __init__(self):
        self.image = pygame.image.load('assets/chars.png')
        self.height = self.image.get_height()

        self.value = 0
        self.high = 0
        self.timer = 0

    def update(self, window, running):
        if running:
            self.timer += 1
            if self.timer >= 6:
                self.timer = 0
                self.value += 1

        text = f'HI {self.high:05d} {self.value:05d}' if self.high else f'{self.value:05d}'

        width = sum(RECTS[CHARS.index(char)][1] + 2 for char in text if char != ' ')
        width += text.count(' ') * 10

        x = SCREEN_WIDTH - 20 - width
        for char in text:
            if char == ' ':
                x += 10
                continue
            left, w = RECTS[CHARS.index(char)]
            window.blit(self.image, (x, 15), (left, 0, w, self.height))
            x += w + 2

    def reset(self):
        self.high = max(self.high, self.value)
        self.value = 0
