import sys
import pygame

from setting import Setting
from ship import Ship

class AlienInvasion:
    """Класс для управлением повидением и ресурсами игры."""

    def __init__(self):
        pygame.init()
        self.settings = Setting()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        
    
    
    
    def _check_events(self):
        """обрабатывает действия в игре, например нажать на крестик"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """при каждом обновлении экрана меняется цвет"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blime()
        self.ship.update()


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_screen()
            #отображение прорисованного экрана
            pygame.display.flip()
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

