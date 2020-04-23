import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu retangulo
        self.image = pygame.image.load('images/tie_fighter_64.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Armazena decimal para centro da espaçonave
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #Flag de movimento
        self.moving_right = self.moving_left = False
        self.moving_up = self.moving_down = False


    def update(self):
        """Atualiza a posição de acordo com a Flag de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        # Atualiza retângulo de acordo com o centro
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)