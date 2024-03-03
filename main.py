import pygame
import sys

WIDTH = 800
HEIGTH = 600

Width_Game = 600
Height_Game = 600



class Snake:
    head_pos = [10, 10]
    vector = 'down'

    def __init__(self):
        self.head_pos = [10, 10]

    def draw_snake(self, a_game):
        pygame.draw.rect(a_game.screen, 'white', (self.head_pos[0], self.head_pos[1], 10, 10))

    def move_snake(self):
        if self.vector == 'down':
            self.head_pos[1] += 1
        elif self.vector == 'up':
            self.head_pos[1] -= 1
        elif self.vector == 'left':
            self.head_pos[0] -= 1
        elif self.vector == 'right':
            self.head_pos[0] += 1

        if self.head_pos[0] >= 605:
            Game.Stop_Game=True
        if self.head_pos[0] <= 5:
            Game.Stop_Game=True
        if self.head_pos[1] >= 605:
            Game.Stop_Game=True
        if self.head_pos[1] <= 5:
            Game.Stop_Game=True

class Game:
    Stop_Game = False


    def __int__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Game test 1')
        self.clock = pygame.time.Clock()

        self.game_border_pass = [5, 5]
        pygame.draw.rect(self.screen, 'blue',(self.game_border_pass[0], self.game_border_pass[1], Width_Game, Height_Game))

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

            #self.screen.fill('black')
            self.game_border_pass = [5, 5]
            pygame.draw.rect(self.screen, 'blue',(self.game_border_pass[0], self.game_border_pass[1], Width_Game, Height_Game))
            snake.move_snake()
            snake.draw_snake(game)
            pygame.display.update()
            pygame.time.wait(10)
            if self.Stop_Game:
                sc = pygame.display.set_mode((800, 600))
                sc.fill((255, 255, 255))

                f1 = pygame.font.Font(None, 36)
                text1 = f1.render('Game Over', 1, (180, 0, 0))

                sc.blit(text1, (10, 50))

                pygame.display.update()

                while 1:
                    for i in pygame.event.get():
                        if i.type == pygame.QUIT:
                            exit()
                sys.exit()



if __name__ == '__main__':
    game = Game()
    game.__int__()
    game.run()
