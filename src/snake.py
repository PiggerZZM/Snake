from src.block import Block


class Snake:

    def __init__(self):
        # 蛇身颜色
        self.color = (255, 255, 255)

        # 蛇运动方向
        self.direction = [10, 0]

        # 蛇身体
        self.blocks = [Block(300, 300), Block(290, 300), Block(280, 300), Block(270, 300), Block(260, 300)]

    def blit_me(self, screen):
        """绘制蛇身"""
        for block in self.blocks:
            block.blit_me(screen, self.color)

    def update(self):
        """更新蛇身"""
        # 这里要了解一下list实现的数据结构，如果改为链表可优化时间复杂度
        self.blocks.pop(-1)
        head = self.blocks[0]
        self.blocks.insert(0, Block(head.pos_x + self.direction[0], head.pos_y + self.direction[1]))
