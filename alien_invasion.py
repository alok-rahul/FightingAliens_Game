#Game Window and respond the User input
import sys
import pygame

class FightAlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Fight Alien Invasion")

    def run_game(self):
        #Start the main loop for  the game
        while True:
            #This is to watch keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    fai = FightAlienInvasion()
    fai.run_game()
