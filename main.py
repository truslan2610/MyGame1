import pygame
import sys

WIDTH = 800
HEIGTH = 600

Width_Game = 600
Height_Game = 600



class Snake:
    head_pos = [10, 10]
    vector = 'down'
    tail_snake = []

    def __init__(self):
        self.head_pos = [100, 100]

    def add_tale(self):
        self.tail_snake.append([21, 10])
        self.tail_snake.append([32, 10])
        self.tail_snake.append([43, 10])
        self.tail_snake.append([54, 10])
        self.tail_snake.append([65, 10])
        self.tail_snake.append([87, 10])
        self.tail_snake.append([98, 10])
        self.tail_snake.append([109, 10])
        self.tail_snake.append([119, 10])
        self.tail_snake.append([130, 10])
        self.tail_snake.append([141, 10])

    def draw_snake(self, a_game):
        pygame.draw.rect(a_game.screen, 'white', (self.head_pos[0], self.head_pos[1], 10, 10))
        # print(f'tail {self.tail_snake}')
        for t in self.tail_snake:
            pygame.draw.circle(a_game.screen, 'white', (t[0]+5,t[1]+5), 5)
            # print(t)


    def move_snake(self):
        back_snake = []
        i = 0
        while i <= len(self.tail_snake) - 1:
            back_snake.append([self.tail_snake[i][0], self.tail_snake[i][1]])
            i += 1

        if self.vector == 'down':
            if len(self.tail_snake) > 0:
                self.tail_snake[0][1] = self.head_pos[1]
                self.tail_snake[0][0] = self.head_pos[0]
            self.head_pos[1] += 10
            i = 1
            while i <= len(self.tail_snake)-1:
                self.tail_snake[i][0] = back_snake[i-1][0]
                self.tail_snake[i][1] = back_snake[i-1][1] #- 10
                i += 1
            # pygame.time.wait(1000)
        elif self.vector == 'up':
            for i, t in enumerate(self.tail_snake):
                if i == 0:
                    t[1] = self.head_pos[1] #+ 10
                    t[0] = self.head_pos[0]
            self.head_pos[1] -= 10
            i = 1
            while i <= len(self.tail_snake)-1:
                self.tail_snake[i][0] = back_snake[i-1][0]
                self.tail_snake[i][1] = back_snake[i-1][1] #+ 10
                i += 1
        elif self.vector == 'left':
            for i, t in enumerate(self.tail_snake):
                if i == 0:
                    t[1] = self.head_pos[1]
                    t[0] = self.head_pos[0] #+ 10
            self.head_pos[0] -= 10
            i = 1
            while i <= len(self.tail_snake)-1:
                self.tail_snake[i][0] = back_snake[i-1][0] #+ 10
                self.tail_snake[i][1] = back_snake[i-1][1]
                i += 1
                # print(f'back {back_snake}')
                # pygame.time.wait(1000)
        elif self.vector == 'right':
            for i, t in enumerate(self.tail_snake):
                if i == 0:
                    t[1] = self.head_pos[1]
                    t[0] = self.head_pos[0] #- 10
            self.head_pos[0] += 10
            i = 1
            while i <= len(self.tail_snake)-1:
                self.tail_snake[i][0] = back_snake[i-1][0] #- 10
                self.tail_snake[i][1] = back_snake[i-1][1]
                i += 1
                # print(f'back {back_snake}')
                # print(f'back tail_snake {self.tail_snake}')
                # pygame.time.wait(1000)

        if self.head_pos[0] >= 605:
            Game.Stop_Game=True
        if self.head_pos[0] <= 5:
            Game.Stop_Game=True
        if self.head_pos[1] >= 605:
            Game.Stop_Game=True
        if self.head_pos[1] <= 5:
            Game.Stop_Game=True

        #Checked tail
        i = 0
        while i <= len(self.tail_snake) - 1:
            tail_x = self.tail_snake[i][0]
            tail_y = self.tail_snake[i][1]

            head_x = self.head_pos[0]
            head_y = self.head_pos[1]
            if self.tail_snake[i] == self.head_pos:
                print(f'tail {self.tail_snake[i]}')
                print(f'head {self.head_pos}')
                Game.Stop_Game = True
            i += 1

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
        snake.add_tale()
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
            pygame.time.wait(100)
            if self.Stop_Game:
                # sc = pygame.display.set_mode((800, 600))
                # sc.fill((255, 255, 255))

                f1 = pygame.font.Font(None, 36)
                text1 = f1.render('Game Over! Press any key!', 1, (180, 0, 0))

                self.screen.blit(text1, (10, 50))

                pygame.display.update()

                while 1:
                    for i in pygame.event.get():
                        if i.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if i.type == pygame.KEYDOWN:
                            pygame.quit()
                            sys.exit()


if __name__ == '__main__':
    game = Game()
    game.__int__()
    game.run()
