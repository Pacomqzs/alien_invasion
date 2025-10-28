import sys

import pygame

from character import Character

class BlueSkye():
    """Simulation of a blue skye background."""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 700))
        self.bg_color = (255, 255, 255)

        pygame.display.set_caption("Blue Sky")

        self.character = Character(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sys.exit()

            # Redraw the screenm during each pass through the loop.
            self.screen.fill(self.bg_color)
            self.character.blitme()
        
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    """Make an isntance of a blue Skye."""
    bk = BlueSkye()
    bk.run_game()