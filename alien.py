import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single  Alien in the fleet"""
    def __init__(self, ai_game):
        """Initialize the alien and set uts starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image abdd set rect attributes
        self.image = pygame.image.load('images/ships.jpeg')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horzontal position
        self.x = float(self.rect.x)
        