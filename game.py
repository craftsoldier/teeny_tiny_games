import os

class Snake:
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction

    def take_step(self, position):
        self.body = [position] + self.body[:-1]

    def set_direction(self, direction):
        self.direction = direction
    def get_head(self):
        return self.body[0] 

class Apple:
    None


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake_object = Snake([((height // 2), (width // 2)), ((height // 2), (width // 2) - 1), ((height // 2), (width // 2) - 2),((height // 2), (width // 2) - 3)], (1,0))

    def board_matrix(self):
        board_matrix = []
        for i in range(self.height):
            rows = []
            for i in range(self.width):
                rows.append(None)
            board_matrix.append(rows)

        for place in self.snake_object.body:
            board_matrix[place[0]][place[1]] = 'O'

        head = self.snake_object.get_head()

        board_matrix[head[0]][head[1]] = 'X'
        return board_matrix

    def play(self):
        while True:
            os.system('clear')
            keys = {'w': (-1,0), 'a': (0,-1), 's': (1, 0), 'd': (0,1)}
            self.render()
            move = input()
            head = self.snake_object.get_head()
            direktion = self.snake_object.direction
            anti_direktion = ((-1) * (direktion[0]), (-1) * direktion[1])
            if move in keys and keys[move] != anti_direktion:
                self.snake_object.set_direction(keys[move])
                direktion = self.snake_object.direction
            new_head = (head[0] + direktion[0], head[1] + direktion[1])
            if new_head in self.snake_object.body:
                os.system('clear')
                print("GAME OVER")
                break
            self.snake_object.take_step(new_head)

    def render(self):
        matrix = self.board_matrix()
        
        print('+', end="")
        for i in range(self.width):
            print('-', end="")
        print('+', end="")
        print()


        for i in range(self.height):
            print('|', end="")
            for k in range(self.width):
                if matrix[i][k] == None:
                    print(" ", end="")
                else:
                    print(matrix[i][k], end="")
            print('|', end="")
            print()
 
        print('+', end="")
        for i in range(self.width):
            print('-', end="")
        print('+', end="")
        print()


game = Game(10, 10)
game.play()

