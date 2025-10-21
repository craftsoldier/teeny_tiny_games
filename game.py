import os
import random

class Snake:
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction

    def move(self, position, grow=False):
        # Add new head position, optionally keep tail (grow) or remove it (move)
        self.body = [position] + (self.body if grow else self.body[:-1])

class Apple:
    def __init__(self, apple_spot):
        self.apple_spot = apple_spot

    def random_spot(self, height, width, body):
        # Generate all positions not occupied by snake
        available = [(r, c) for r in range(height) for c in range(width) if (r, c) not in body]
        self.apple_spot = random.choice(available) if available else (0, 0)  # Fallback if board full
        return self.apple_spot

class Game:
    def __init__(self, height, width):
        self.height, self.width = height, width
        r, c = random.randint(2, height - 3), random.randint(4, width - 5)
        self.snake = Snake([(r, c), (r, c-1), (r, c-2), (r, c-3)], (0, 0))
        self.apple = Apple((0, 0))
        self.apple.random_spot(height, width, self.snake.body)
        self.score = 0

    def board_matrix(self):
        # Create empty board
        matrix = [[None] * self.width for _ in range(self.height)]
        # Place snake body, then head, then apple
        for r, c in self.snake.body:
            matrix[r][c] = 'O'
        head = self.snake.body[0]
        matrix[head[0]][head[1]] = 'X'
        matrix[self.apple.apple_spot[0]][self.apple.apple_spot[1]] = 'A'
        return matrix

    def play(self):
        keys = {'w': (-1,0), 'a': (0,-1), 's': (1, 0), 'd': (0,1)}
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.render()
            move = input()
            head, direktion = self.snake.body[0], self.snake.direction
            anti = (-direktion[0], -direktion[1])
            if move in keys and keys[move] != anti:
                direktion = self.snake.direction = keys[move]
            if direktion == (0, 0):
                continue
            new_head = ((head[0] + direktion[0]) % self.height, (head[1] + direktion[1]) % self.width)
            if new_head in self.snake.body:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("GAME OVER")
                break
            # Eat apple or move
            if new_head == self.apple.apple_spot:
                self.score += 1
                self.snake.move(new_head, grow=True)
                self.apple.random_spot(self.height, self.width, self.snake.body)
            else:
                self.snake.move(new_head)

    def render(self):
        matrix = self.board_matrix()
        border = '+' + '-' * self.width + '+'
        print(border)
        for row in matrix:
            print('|' + ''.join(cell if cell else ' ' for cell in row) + '|')
        print(f"{border}\n\n\nScore: {self.score}")

game = Game(10, 10)
game.play()