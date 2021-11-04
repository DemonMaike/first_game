'''Класс настроек'''

class Setting:
    """Класс для создания объекта настроек игры"""
    def __init__(self):
        # Изображение
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Корабль
        self.ship_speed = 1.5
        self.ship_limits = 1.5
        # Снаряд
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        #Алиены
        self.alien_speed = 0.1
        self.fleet_drop_speed = 100
        self.fleet_direction = 1
        # Темп ускорения игры
        self.speedup_scale = 1.10
        # если 1 - вправо, если -1 -влево.
        self.fleet_direction = 1

    def init_start_setting(self):
         """Инициализирует настройки, изменяющиеся в ходе игры."""
         self.ship_speed_factor = self.ship_speed
         self.bullet_speed_factor = self.bullet_speed
         self.alien_speed_factor = self.alien_speed
        
    def incrace_speed(self):
        '''Увеличивает настройки скорости'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

            
        
