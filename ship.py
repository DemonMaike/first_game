import pygame

class Ship:
    """Класс для управления караблём"""
    def __init__(self, ai_game):
        self.screen  = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('./image/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.settigs = ai_game.settigs
        self.x = float(self.rect.x)
    

    def blime(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        '''Обнавляет позицию корабля с учётом флагов'''
        # Обновляет x, не rect

        if self.moving_right:
            self.x += self.settigs.ship_speed

        if self.moving_left:
            self.x -= self.settigs.ship_speed
