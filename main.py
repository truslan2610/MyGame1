import pygame
import sys

WIDTH = 800
HEIGTH = 600


class Snake:
    head_pos = [10, 10]
    vector = 'down'

    def __init__(self):
        self.head_pos = [10, 10]

    def draw_snake(self, a_game):
        pygame.draw.rect(a_game.screen, 'white', (self.head_pos[0], self.head_pos[1], 10, 10))

    def move_snake(self):
        if self.vector == 'down':
            self.head_pos[1] += 10
        elif self.vector == 'up':
            self.head_pos[1] -= 10
        elif self.vector == 'left':
            self.head_pos[0] -= 10
        elif self.vector == 'right':
            self.head_pos[0] += 10


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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        snake.vector = 'down'
                    if event.key == pygame.K_UP:
                        snake.vector = 'up'
                    if event.key == pygame.K_LEFT:
                        snake.vector = 'left'
                    if event.key == pygame.K_RIGHT:
                        snake.vector = 'right'
                # print(event)

            self.screen.fill('black')
            snake.move_snake()
            snake.draw_snake(game)
            pygame.display.update()
            pygame.time.wait(500)


if __name__ == '__main__':
    game = Game()
    game.__int__()
    game.run()
