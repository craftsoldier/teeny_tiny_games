#this is tetris btw

import random

class Piece:
    def __init__(self):
        self.piece_list = ['i', 'j', 'l', 'o', 's', 'z', 't']
        self.piece_coords = { 'i': [(-2, 0), (-1, 0), (0, 0), (1, 0)],
                              'j': [(-1, -1), (-1, 0), (0, 0), (1, 0)],
                              'l': [(-1, 0), (0, 0), (1, 0), (1, 1)],
                              'o': [(-1, -1), (-1, 0), (0, 0), (0, 1)],
                              's': [(-1, 0), (0, 0), (0, 1), (1, 1)],
                              'z': [(-1, -1), (-1, 0), (0, 0), (1, 0)],
                              't': [(-1, 0), (0, -1), (0, 0), (0, 1)]
                             }
       
    def rotate(self, tetromino, angle):
        rotation_list = self.piece_coords[tetromino]
        new_coords = []
        for (x, y) in rotation_list:
            if angle == 1: 
                new_coord = (y, -x)
            elif angle == -1:
                new_coord = (-y, x)
            new_coords.append(new_coord)
        rotation_list = new_coords
        return rotation_list

    def random_bag(self):
        bag_pieces = [random.randint(0,6) for i in range(10)]
        return bag_pieces


class Board:
    def __init__(self):
        self.height = 20
        self.width = 10
        self.grid = [[0] * self.width for _ in range(self.height)]
        self.pieces = Piece()
        self.current_piece = None
        self.current_position = None
        self.current_coords = None

    def spawn_piece(self, piece_type):
    
    def display_piece(self, piece, position):
        if piece in self.pieces.piece_coords:
            piece_list = self.pieces.piece_coords[piece]
        piece_place = [(x + position[0], y + position[1]) for x, y in self.pieces.piece_coords[piece]]
        for pawn in piece_place:    
            self.grid[pawn[0]][pawn[1]] = 1
        
        
    def display_board(self):
        print()
        print()
        for i in range(self.height):
            print('|', end='')
            for k in range(self.width):
                if self.grid[i][k] == 0:
                    print('  ', end='')
                if self.grid[i][k] == 1:
                    print('##', end='')
            print('|')
        print(' ', end='')
        for j in range(self.width - 1):
            print('--', end='')
        print('--')

    def play(self):
        bags = self.pieces.random_bag()





game = Board()
game.display_piece('t', (5,3))
game.display_board()
piece = Piece()

print(piece.rotate('t', 1))
