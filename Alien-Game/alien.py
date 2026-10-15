import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Move the alien horizontally."""

        self.x += (
            self.ai_settings.alien_speed
            * self.ai_settings.fleet_direction
        )

        self.rect.x = round(self.x)