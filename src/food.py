import pygame
from pygame.sprite import Sprite
from random import randint


class Food(Sprite):

    def __init__(self, settings):
        super(Food, self).__init__()
        self.width = 10
        self.height = 10
        self.color = (0, 255, 255)

        self.pos_x = randint(self.height, settings.screen_height - self.height) // 10 * 10
        self.pos_y = randint(self.width, settings.screen_width - self.width) // 10 * 10

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.pos_x
        self.rect.left = self.pos_y

    def blit_me(self, screen):
        screen.fill(self.color, self.rect)

    def regenerate(self, settings):
        self.pos_x = randint(self.height, settings.screen_height - self.height) // 10 * 10
        self.pos_y = randint(self.width, settings.screen_width - self.width) // 10 * 10

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.pos_x
        self.rect.left = self.pos_y
