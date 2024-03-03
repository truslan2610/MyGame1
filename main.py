import pygame, sys

WIDTH = 800
HEIGTH = 600

class Snake:
    head_pos = [10, 10]

    def __init__(self):
        head_pos = [10, 10]

    def draw_snake(self, game):
        pygame.draw.rect(game.screen, 'white', (self.head_pos[0], self.head_pos[1], 10, 10))

    def move_snake(self):
        self.head_pos[1] += 10

class Game:
    def __int__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Game test 1')
        self.clock = pygame.time.Clock()

    def run(self):
        snake = Snake()
        snake.__init__()
        snake.draw_snake(game)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            snake.move_snake()
            snake.draw_snake(game)
            pygame.display.update()
            pygame.time.wait(1000)


if __name__ == '__main__':
    game = Game()
    game.__int__()
    game.run()
