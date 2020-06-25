import pygame
from pygame.sprite import Sprite


class Block(Sprite):

    def __init__(self, pos_x, pos_y):
        super(Block, self).__init__()
        # 方块的大小
        self.width = 10
        self.height = 10

        # 方块的坐标
        self.pos_x = pos_x
        self.pos_y = pos_y

        # 方块对应的Rect对象
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.pos_x
        self.rect.left = self.pos_y

    def blit_me(self, screen, color):
        """绘制方块"""
        screen.fill(color, self.rect)
