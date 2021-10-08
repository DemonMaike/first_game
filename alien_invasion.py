import sys
import pygame
from time import sleep

from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

class AlienInvasion:
    """Класс для управлением повидением и ресурсами игры."""
    def __init__(self):
        pygame.init()
        self.settings = Setting()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        if self.stats.ships_left > 0:
            # Уменьшение жизней
            self.stats.ships_left -= 1
            # Отчистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()
            # Создать новый корабль в центре и флот
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.stats.game_active = False


        # Пауза
        sleep(0.5)
    
    def _create_fleet(self):
        """Создание флота пришельцев"""
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Определяет колличество рядов, помещающихся на экране
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
        (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Cоздание флота вторжения
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        """Создание пришельца в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.bullets.update()
                self._update_aliens()
                self._check_fleet_edges()
                self._update_bullets()
            self._update_screen()
            #отображение прорисованного экрана
            pygame.display.flip() 
    
    def _update_bullets(self):
        #удаляем снаряды за пределом поля
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        #Обнаружение попадания в пришельца, если да, убрать алиена
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление его движения"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте"""
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #Если добрались алиены добрались до земли, то проигрыш
        self._check_aliens_bottom()

    def _check_events(self):
        """обрабатывает действия в игре, например нажать на крестик"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Обрабатывает нажатия кнопок"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
               self._fire_bullet()
    
    def _fire_bullet(self):
        """Создание снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _check_keyup_events(self, event):
        """Обрабатывает событие отпущенной кнопки"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """при каждом обновлении экрана меняется цвет"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blime()
        self.ship.update()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
    
    def _check_aliens_bottom(self):
        """Проверяет, добрались ли до нижнего края алиены"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
