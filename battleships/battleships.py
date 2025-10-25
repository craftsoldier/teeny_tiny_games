import os
import random

class Board:
    def __init__(self):
        self.height = 10
        self.width = 10
        self.ship_list = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
        self.ship_dic = {'carrier': 5,
                  'battleship': 4, 
                  'cruiser': 3, 
                  'submarine': 3, 
                  'destroyer': 2 }
        self.ship_shape_list = ['X', '#', '$', '@', '0']
        self.ship_shape = {'carrier': 'X',
                           'battleship': '#',
                           'cruiser': '$',
                           'submarine': '@',
                           'destroyer': '0'}

    def place_ships(self):
        board  = [[None] * self.width for _ in range(self.height)]

        for ship in self.ship_list:
            formation_incomplete = True

            while formation_incomplete:
                direction_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                ship_coords = []

                random_coord = (random.randint(0, 9), random.randint(0, 9))
                random_direction = direction_list[(random.randint(0, 3))]

                for i in range(self.ship_dic[ship]):
                    valid_formation = True

                    if board[random_coord[0]][random_coord[1]] == None:
                        ship_coords.append(random_coord)

                        if i < self.ship_dic[ship] - 1:
                            x, y = (random_coord[0] + random_direction[0]), (random_coord[1] + random_direction[1])

                            if not( 0 <= x < self.height and 0 <= y < self.width):
                                valid_formation = False
                                break

                            random_coord = (x, y)
                    else:
                        valid_formation = False
                        break

                if valid_formation:
                    for coord in ship_coords:
                        board[coord[0]][coord[1]] = self.ship_shape[ship]
                    formation_incomplete = False

        return board

    def draw_board(self, board):
        print("\n ", end="   ")

        for i in range(ord('A'), ord('J') + 1):
            letter = chr(i)
            print(letter, end = ' ')
        print()
        print(" " * 3 + "-" * 21)
        for i in range(self.height):
            print(f"{i+1:<2}|", end=" ")
            for k in range(self.width):
                if board[i][k] == None:
                    print('⋅', end = ' ')
                else:
                    print(board[i][k], end = ' ')
            print('|')
        print(" " * 3 + "-" * 21)

    def draw_player_board(self, board, shot_list = None):
        if shot_list != None:
            for shot in shot_list:

                x, y = shot[0], shot[1]

                if board[x][y] in self.ship_shape_list:
                    board[x][y] = 'H'
                elif board[x][y] == None:
                    board[x][y] = 'M'

            self.draw_board(board)
        else:
            self.draw_board(board)

    def draw_opponent_board(self, board, shot_list = None):
        if shot_list != None:
            for shot in shot_list:

                x, y = shot[0], shot[1]

                if board[x][y] in self.ship_shape_list:
                    board[x][y] = 'H'
                elif board[x][y] == None:
                    board[x][y] = 'M'

            board = [[None if cell in self.ship_shape_list  else cell for cell in row] for row in board]
            self.draw_board(board)
        else:
            board = [[None if cell in self.ship_shape_list else cell for cell in row] for row in board]
            self.draw_board(board)

    def check_winner(self, board):
        count = 0
        for i in range(self.height):
            for k in range(self.width):
                if board[i][k] == 'H':
                    count += 1
        if count == 17:
            return True
        else:
            return False

class Game:
    def __init__(self):
        self.board = Board()
        self.board_one = self.board.place_ships()
        self.board_two =  self.board.place_ships()
        self.shot_list = [[], []]

    def get_shot(self):
        try:
            shot = input("enter shot: ") 
            x = ord(shot[0].upper()) - ord('A')
            y = int(shot[1:]) - 1

            if not (0 <= x < 10 and 0 <= y < 10):
                raise
            return (y, x)

        except:
            return self.get_shot()

    def draw_turn(self, board, shot_list, number):
        self.board.draw_player_board(board[number], shot_list[1 - number])
        self.board.draw_opponent_board(board[1 - number], shot_list[number])

    def play(self):
        player = 0
        board = [self.board_one, self.board_two]

        os.system('clear')
        while True:
            os.system('clear')
            print(f"Player {player + 1}")
            self.draw_turn(board, self.shot_list, player)
       
            shot = self.get_shot()
            if shot in self.shot_list[player]:
                print("duplicate shot..")
                continue


            os.system('clear')
            print(f"Player {player + 1}")
            self.shot_list[player].append(shot)
            self.draw_turn(board, self.shot_list, player)

            if self.board.check_winner(board[1 - player]):
                os.system('clear')
                print(f"Player {player + 1} WINS!")
                break
            
            input("press enter..")
            player = 1 - player 
            


game = Game()
game.play()

