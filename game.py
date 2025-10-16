

class Snake:
    None

class Apple:
    None

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board_matrix(self):
        board_matrix = []
        for i in range(self.height):
            rows = []
            for i in range(self.width):
                rows.append(None)
            board_matrix.append(rows)
        return board_matrix

    def render(self):
        matrix = self.board_matrix()

        print(f"Height: {self.height}")
        print(f"Width: {self.width}")


game = Game(10 ,20)
game.render()
