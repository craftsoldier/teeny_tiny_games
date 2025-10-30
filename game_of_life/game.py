import random
import time
import os

class Game:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.board = [[1] * self.width for _ in range(self.height)]
        self.direction_list = [(0, 1), (1, 1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (0, -1)]

    def dead_state(self):
        return [[0] * self.width for _ in range(self.height)]

    def random_state(self):
        for i in range(self.height):
            for k in range(self.width):
                self.board[i][k] = random.randint(0, 1)

    def next_state(self):
        next_board = self.dead_state()

        for i in range(self.height):
            for k in range(self.width):
                counter = 0

                for direction in self.direction_list:
                    if 0 <= (i + direction[0]) < self.height and 0 <= (k+direction[1]) < self.width:
                        if self.board[i + direction[0]][k + direction[1]] == 1:
                            counter += 1

                if self.board[i][k] == 1:
                    if 0 <= counter < 2:
                        next_board[i][k] = 0
                    elif 2 <= counter < 4:
                        next_board[i][k] = 1 
                    elif counter > 3:
                        next_board[i][k] = 0

                if self.board[i][k] == 0:
                    if counter == 3:
                        next_board[i][k] = 1

        self.board = next_board

    def render(self):
        board = self.board
        for i in range(self.width):
            print('--', end='')

        print()
       
        for i in range(self.height):
            for k in range(self.width):
                if board[i][k] == 0:
                    print(' ', end = ' ')
                elif board[i][k] == 1: 
                    print('#', end = ' ')
            print()

        for i in range(self.width):
            print('--', end='')
        print()

    def run_life(self):
        self.random_state()
        while True:
            self.render()
            time.sleep(1)
            os.system('clear')
            self.next_state()

game = Game()
game.run_life()
