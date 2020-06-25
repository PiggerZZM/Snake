from src.block import Block
from src.game_function import eat_food


class Snake:

    def __init__(self):
        # 蛇身颜色
        self.color = (255, 255, 255)

        # 蛇运动方向
        self.direction = [10, 0]

        # 蛇身体
        self.blocks = [Block(300, 300), Block(290, 300), Block(280, 300), Block(270, 300), Block(260, 300)]

        # 蛇头
        self.head = self.blocks[0]

    def blit_me(self, screen):
        """绘制蛇身"""
        for block in self.blocks:
            block.blit_me(screen, self.color)

    def update(self, food, settings):
        """更新蛇身"""
        # 这里要了解一下list实现的数据结构，如果改为链表可优化时间复杂度
        if not eat_food(self, food, settings):
            self.blocks.pop(-1)
        old_head = self.blocks[0]
        self.blocks.insert(0, Block(old_head.pos_x + self.direction[0], old_head.pos_y + self.direction[1]))
        self.head = self.blocks[0]

    def regenerate(self):
        self.blocks = [Block(300, 300), Block(290, 300), Block(280, 300), Block(270, 300), Block(260, 300)]
        self.head = self.blocks[0]
        self.direction = [10, 0]
