import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс снаряда"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colors = self.settings.bullet_color
        #Создание снаряда в позиции (0, 0) и задание направления
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
         self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)
    
    def update(self):
        """Движение снаряда"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.colors, self.rect)