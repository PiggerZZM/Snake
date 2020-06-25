import pygame
import sys
import logging


def check_events(play_button, stats, snake):
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            exit_game()

        # 监听鼠标
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, stats, mouse_x, mouse_y)

        # 监听键盘
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.direction = [0, 10]
            elif event.key == pygame.K_LEFT:
                snake.direction = [0, -10]
            elif event.key == pygame.K_UP:
                snake.direction = [-10, 0]
            elif event.key == pygame.K_DOWN:
                snake.direction = [10, 0]


def exit_game():
    sys.exit()


def update_screen(screen, settings, play_button, stats, snake, wall, food):
    # 重绘屏幕
    screen.fill(settings.bg_color)

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button(screen)
    else:
        # 重绘围墙
        wall.blit_me(screen)
        # 重绘蛇身
        snake.blit_me(screen)
        # 重绘食物
        food.blit_me(screen)

    # 刷新屏幕
    pygame.display.flip()


def check_play_button(play_button, stats, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 开始游戏
        start_game(stats)


def start_game(stats):
    # 游戏状态为开始
    stats.game_active = True

    # 隐藏光标
    pygame.mouse.set_visible(False)


def check_snake_wall(snake, food, wall, stats, settings):
    if pygame.sprite.spritecollideany(snake.head, wall.blocks):
        game_over(snake, food, stats, settings)
        logging.info('撞墙了')


def check_snake_snake(snake, food, stats, settings):
    for block in snake.blocks:
        if block is not snake.head and (snake.head.pos_x, snake.head.pos_y) == (block.pos_x, block.pos_y):
            game_over(snake, food, stats, settings)
            logging.info('撞身体了')
            break


def game_over(snake, food, stats, settings):
    stats.game_active = False
    snake.regenerate()
    food.regenerate(settings)


def eat_food(snake, food, settings):
    if (snake.head.pos_x, snake.head.pos_y) == (food.pos_x, food.pos_y):
        logging.info("吃食物了")
        food.regenerate(settings)
        return True
    else:
        return False

