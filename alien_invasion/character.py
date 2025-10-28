import pygame

class Character:
    """A class to manage the character."""

    def __init__ (self, bk):
        """Initialize the character and 
        set its individual position.
        """
        self.screen = bk.screen
        self.screen_rect = bk.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/game_character.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)