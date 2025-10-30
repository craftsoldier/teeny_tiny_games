import os

class Board:
    def __init__(self):
        self.height = 6
        self.width = 7
        self.color_codes = { 1: '\033[97m●\033[0m',
                             0: '\033[90m●\033[0m'}

    def make_move(self, board, move, player):
        for i in range(self.height - 1, -1, -1):
            if board[i][move - 1] is None:
                board[i][move - 1] = player
                return True
        return False

    def draw_board(self, board):
        print(" ┌" + "─" * (self.width * 2 + 1) + "┐")
        for row in board:
            print(" │ ", end='')
            for cell in row:
                print('⋅' if cell is None else self.color_codes[cell], end=' ')
            print("│")
        print(" └" + "─" * (self.width * 2 + 1) + "┘")
        print("   " + " ".join(str(i) for i in range(1, self.width + 1)))

class Game:
    def __init__(self):
        self.board = Board()
        self.main_board = [[None] * self.board.width for _ in range(self.board.height)]

    def get_move(self):
        try:
            move = int(input("enter move (1-7): "))
            if 1 <= move <= 7:
                return move
            print("invalid column!")
            return self.get_move()
        except ValueError:
            print("enter a number!")
            return self.get_move()

    def check_win(self, board):
        direction_list = [(1, 0), (0, 1), (1, 1), (-1, 1)]

        for dr, dc in direction_list:
            for row in range(self.board.height):
                for col in range(self.board.width):
                    end_row = row + 3 * dr
                    end_col = col + 3 * dc

                    if end_row < 0 or end_row >= self.board.height:
                        continue
                    if end_col < 0 or end_col >= self.board.width:
                        continue

                    if board[row][col] is None:
                        continue

                    if (board[row][col] == board[row + dr][col + dc] ==
                        board[row + 2*dr][col + 2*dc] == board[row + 3*dr][col + 3*dc]):
                        return True

        return False

    def play(self):
        player = 0
        while True:
            os.system('clear')
            print(f"player {player + 1}'s turn")
            self.board.draw_board(self.main_board)

            move = self.get_move()
            if not self.board.make_move(self.main_board, move, player):
                print("column full!")
                input("press enter...")
                continue

            if self.check_win(self.main_board):
                os.system('clear')
                self.board.draw_board(self.main_board)
                print(f"Player {player + 1} wins!")
                break

            player = 1 - player


game = Game()
game.play()
