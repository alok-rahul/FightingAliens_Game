import pygame
class Ship:

    def __init__(self, fai_game):
        """Initialize the ship and set starting position"""
        self.screen = fai_game.screen
        self.screen_rect = fai_game.screen.get_rect()

        # Load the image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen

        self.rect.midbottom = self.screen_rect.midbottom

    def blitime(self):
        """Draw the car at the current location. """
        self.screen.blit(self.image, self.rect)