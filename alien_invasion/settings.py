# -*- coding: UTF-8 -*-
class Settings:
    """ Uma classe para armazenar todas as configurações """

    def __init__(self):
        """Inicializa as configurações do jogo"""

        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (23, 23, 46)

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5

        # Configuração dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
