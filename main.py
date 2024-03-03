import pygame, sys

WIDTH = 800
HEIGTH = 600


class Game:
    def __int__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Game test 1')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.__int__()
    game.run()
