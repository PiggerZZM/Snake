from pygame.sprite import Group

from src.block import Block


class Wall:

    def __init__(self, settings):
        self.width = 10
        self.height = 10
        self.color = (0, 0, 255)

        self.blocks = Group()
        self.add_block(settings)

    def blit_me(self, screen):
        """绘制墙体"""
        for block in self.blocks.sprites():
            block.blit_me(screen, self.color)

    def add_block(self, settings):
        for x in range(0, settings.screen_height, self.height):
            if x == 0 or x == settings.screen_height - self.height:
                for y in range(0, settings.screen_width, self.width):
                    self.blocks.add(Block(x, y))
            else:
                self.blocks.add(Block(x, 0))
                self.blocks.add(Block(x, settings.screen_width - self.width))
