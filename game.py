import pygame

from const import *
from dino import Dino
from ground import Ground
from cloud import Cloud
from score import Score


class Game:

    def __init__(self):
        self.ingame = False
        self.game_over = False

        self.dino = Dino(96, 0)
        self.ground = Ground()
        self.cloud = Cloud()
        self.score = Score()

        self.game_over_image = pygame.image.load('assets/game_over.png')
        self.restart_image = pygame.image.load('assets/restart_button.png')

    def update(self, window, keys):
        if (keys.get(pygame.K_SPACE) or keys.get(pygame.K_UP)) and not self.ingame:
            self.start()
        elif (keys.get(pygame.K_SPACE) or keys.get(pygame.K_UP)) and self.game_over:
            self.restart()

        self.dino.update(window, keys)

        if self.ingame and not self.dino.is_jumping and not self.ground.move and not self.game_over:
            self.ground.move = True

        self.cloud.update(window, self.ground.move)

        if self.ingame:
            self.ground.update(window, self.score.value)
            self.score.update(window, not self.game_over)

        for obstacle in self.ground.obstacles:
            image = self.ground.bird_frames[obstacle['frame']] if obstacle['type'] == 'bird' else obstacle['image']
            dino = self.dino.image
            if pygame.Rect(obstacle['x'], obstacle['y'], *image.get_size()).colliderect(
                pygame.Rect(self.dino.x, self.dino.y, *dino.get_size())
            ):
                self.game_over = True
                self.ground.move = False
                self.dino.game_over = True

        if self.game_over:
            window.blit(self.game_over_image, (SCREEN_WIDTH // 2 - self.game_over_image.get_width() // 2, 70))
            window.blit(self.restart_image, (SCREEN_WIDTH // 2 - self.restart_image.get_width() // 2, 95))

    def start(self):
        self.ingame = True
        self.dino.start()

    def restart(self):
        self.ingame = False
        self.game_over = False

        self.score.reset()
        self.ground.reset()
        self.cloud.reset()
        self.dino.reset()
