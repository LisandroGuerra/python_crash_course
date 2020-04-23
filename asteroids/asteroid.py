
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # Inicia o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Asteroid')

    # Cria uma nave
    ship = Ship(ai_settings, screen)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()
