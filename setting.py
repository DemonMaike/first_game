'''Класс настроек'''

class Setting():
    """Класс для создания объекта настроек игры"""
    def __init__(self):
        # Изображение
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Корабль
        self.ship_speed = 1.5
        self.ship_limits = 3
        # Снаряд
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        #Алиены
        self.alien_speed = 1.5
        self.fleet_drop_speed = 100
        self.fleet_direction = 1
    