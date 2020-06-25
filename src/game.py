import pygame
import logging

from src.food import Food
from src.game_function import check_snake_wall, check_snake_snake
from src.game_stats import GameStats
from src.settings import Settings
from src import game_function as gf
from src.button import Button
from src.snake import Snake
from src.wall import Wall

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def run_game():
    # 初始化
    pygame.init()
    logging.info('Pygame初始化成功')

    # 实例化游戏设置类
    settings = Settings()
    logging.info('实例化游戏设置成功')

    # 创建屏幕对象
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption)
    logging.info('创建屏幕成功')

    # 创建开始按钮
    play_button = Button()
    logging.info('实例化开始按钮成功')

    # 创建贪吃蛇对象
    snake = Snake()
    logging.info('实例化贪吃蛇成功')

    # 创建围墙对象
    wall = Wall(settings)
    logging.info('实例化围墙成功')

    # 创建统计信息
    stats = GameStats()
    logging.info('实例化统计信息成功')

    # 创建食物
    food = Food(settings)
    logging.info('实例化食物成功')

    # 控制窗口刷新速度
    fps = 10
    clock = pygame.time.Clock()

    # 游戏主循环
    while True:
        # 监听事件
        gf.check_events(play_button, stats, snake)

        if stats.game_active:
            # 更新蛇身
            snake.update(food, settings)
            # 检查蛇头与墙壁碰撞
            check_snake_wall(snake, food, wall, stats, settings)
            # 检查蛇头与蛇身碰撞
            check_snake_snake(snake, food, stats, settings)

        # 重绘屏幕
        gf.update_screen(screen, settings, play_button, stats, snake, wall, food)

        # 控制窗口刷新速度
        clock.tick(fps)


if __name__ == '__main__':
    run_game()
