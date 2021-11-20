import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        """Initialize the aliens and position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loading aline image
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # define aline starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Storing alien position

        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if aline is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Moving alien right and left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
