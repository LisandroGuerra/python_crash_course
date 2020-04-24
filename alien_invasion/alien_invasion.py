# -*- coding: UTF-8 -*-
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game():
    # Inicia o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Cria uma nave
    ship = Ship(ai_settings, screen)
    # Cria grupo para armazenar projéteis
    bullets = Group()

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

        # Deixa a tela mais recente visível
        pygame.display.flip()


run_game()
