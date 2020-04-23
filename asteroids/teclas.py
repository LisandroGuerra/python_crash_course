# -*- coding: UTF-8 -*-
import pygame
import sys


class Settings:
    """ Uma classe para armazenar todas as configurações """

    def __init__(self):
        """Inicializa as configurações do jogo"""

        # Configurações da tela
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)


def check_events():
    """Responde a pressionamento de teclado e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event is not None:
                return event.key


def update_screen(ai_settings, screen):
    """Redesenha a tela a cada passagem pelo laço"""
    screen.fill(ai_settings.bg_color)


def run_game():
    # Inicia o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Teclas')

    # Cria uma nave
    # ship = Ship(ai_settings, screen)

    # Inicia o laço principal do jogo
    while True:
        key = check_events()
        print(key)
        # ship.update()
        update_screen(ai_settings, screen)

        # Deixa a tela mais recente visível
        pygame.display.flip()


run_game()
