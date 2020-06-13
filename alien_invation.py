# _*_ coding:utf-8 _*_
# 开发团队:
# 开发人员：Administrator
# 开发时间：2020/6/923:15
# 文件名称：alien_invation
# 开发工具：PyCharm

import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 验证子弹是否正确删除
        # print(len(bullets))
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship,aliens, bullets)


run_game()
