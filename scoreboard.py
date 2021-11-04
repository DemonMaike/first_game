import pygame.font

class Scoreboard:
    '''Класс для вывода игровой информации.'''
    def __init__(self,ai_game):
        '''Инциализируем атрибуты подсчёта очков'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        #Настройки шрифта для вывода счёта
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #Подготовка исходного изображения
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    
    def prep_score(self):
        '''Преобразует текущий счёт в графическое изображение.'''
        #Вывод счёта в правой верхней части экрана
        
    
    def show_score(self):
        '''Выводит счёт на экран'''
        self.screen.blit(self.score_image,self.score_rect)


