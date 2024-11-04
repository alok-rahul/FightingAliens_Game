#Game Window and respond the User input
import sys
import pygame

from settings import Settings
from ship import Ship

class FightAlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Fight Alien Invasion")
        self.ship = Ship(self)
        #Display Color
        self.bg_color = (230,230,230)

    def run_game(self):
        #Start the main loop for  the game
        while True:
            #This is to watch keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen during each pass through the loop 
            self.screen.fill(self.settings.bg_color)
            self.ship.blitime()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    fai = FightAlienInvasion()
    fai.run_game()
