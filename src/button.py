import pygame.ftfont


class Button:

    def __init__(self, msg='Play'):
        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.ftfont.SysFont(None, 48)
        self.msg = msg
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def draw_button(self, screen):
        """绘制一个用颜色填充的按钮，再绘制文本"""

        # 创建按钮的rect对象，并使其居中
        self.rect.center = screen.get_rect().center

        # 绘制按钮
        screen.fill(self.button_color, self.rect)

        # 将msg渲染为图像，并使其在按钮上居中
        msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        msg_image_rect = msg_image.get_rect()
        msg_image_rect.center = screen.get_rect().center

        # 绘制文本
        screen.blit(msg_image, msg_image_rect)
