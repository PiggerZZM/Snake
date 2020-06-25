import pygame

from src.food import Food
from src.game_stats import GameStats
from src.settings import Settings
from src import game_function as gf
from src.button import Button
from src.snake import Snake
from src.wall import Wall


def run_game():
    # 初始化
    pygame.init()

    # 实例化游戏设置类
    settings = Settings()

    # 创建屏幕对象
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption)

    # 创建开始按钮
    play_button = Button()

    # 创建贪吃蛇对象
    snake = Snake()

    # 创建围墙对象
    wall = Wall(settings)

    # 创建统计信息
    stats = GameStats()

    # 创建食物
    food = Food(settings)

    # 控制窗口刷新速度
    fps = 10
    clock = pygame.time.Clock()

    # 游戏主循环
    while True:
        # 监听事件
        gf.check_events(play_button, stats, snake)

        # 更新蛇身
        snake.update()

        # 重绘屏幕
        gf.update_screen(screen, settings, play_button, stats, snake, wall, food)

        # 控制窗口刷新速度
        clock.tick(fps)


if __name__ == '__main__':
    run_game()
