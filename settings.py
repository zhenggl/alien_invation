# _*_ coding:utf-8 _*_
# 开发团队:
# 开发人员：Administrator
# 开发时间：2020/6/923:27
# 文件名称：settings
# 开发工具：PyCharm


class Settings:
    """存储《外星人入侵》的所有设置类"""

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3 #可用飞船数量
        # 子弹的设置
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_speed_factor = 3
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，-1表示向左移动
        self.fleet_direction =1
