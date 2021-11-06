
class GameStats:
    """Отслеживание статистики игры"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        # Не збрасывается рекорд.
        self.high_score = 0
        self.level = 0
        
    def reset_stats(self):
        """Инциализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = int(self.settings.ship_limits)
        self.score = 0
