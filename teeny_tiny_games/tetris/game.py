import os
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
       
    def rotate(self, tetromino, original_coords, direction):
        if direction == 1:
            new_coords  = []
            for (x, y) in original_coords:
                new_coord = (y, -x)
                new_coords.append(new_coord)

        elif direction == -1:
            new_coords = []
            for (x, y) in original_coords:
                new_coord = (-y, x)
                new_coords.append(new_coord)
        return new_coords

    def random_bag(self):
        bag_numbers = [random.randint(0,6) for i in range(10)]
        bag_pieces = [self.piece_list[bag] for bag in bag_numbers]
        return bag_pieces


class Board:
    def __init__(self):
        self.height = 20
        self.width = 10
        self.grid = [[0] * self.width for _ in range(self.height)]
        self.pieces = Piece()
        self.current_piece = None
        self.current_position = None
        self.current_coords = []

    def spawn_piece(self, piece_type):
        self.current_piece = piece_type
        self.current_position = (2, 4)
        self.current_coords = self.pieces.piece_coords[piece_type]

    def move_down(self, position):
        return (position[0] + 1, position[1])

    def move_sideways(self, position, direction):
        if direction > 0:
            return (position[0], position[1] - 1)
        elif direction < 0:
            return (position[0], position[1] + 1)

    def collision_check(self, coords, position):
        for (x, y) in coords:
            x_ash = position[0] + x
            y_ash = position[1] + y
            if (x_ash < 0 or x_ash >= self.height) or (y_ash < 0 or y_ash >= self.width): 
                return False
            if self.grid[x_ash][y_ash] == 1:
                return False
        return True
    
    def display_piece(self, position):
        for y, x in self.current_coords:    
            self.grid[position[0] + y][position[1] + x] = 1

    def clear_piece(self, position):
        for y, x in self.current_coords:
            self.grid[position[0] + y][position[1] + x] = 0
        
    def display_board(self):
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

    def game_over(self):
        if not self.collision_check(self.current_coords, self.current_position):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("GAME OVER")
            return True
        return False


    def garbage_collector(self):
        garbage = True
        while garbage:
            garbage = False
            for i in range(self.height):
                row_full = True
                for k in range(self.width):
                    if self.grid[i][k] == 0:
                        row_full = False
                        break
                if row_full:
                    del self.grid[i]
                    self.grid.insert(0, [0] * self.width)
                    garbage = True
                    break

    def play(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        bags = self.pieces.random_bag()
        bag_int = 0

        self.spawn_piece(bags[bag_int])
        self.display_piece(self.current_position)
        self.display_board()

        move_list = { 'w': 0,
                      'a': 2, #left
                      's': 0,
                      'd': -2, #right
                      'z': -1, #ccw
                      'x': 1, #cw
                      ' ': 999} #hard-drop

        while True:
            move = input()
            os.system('cls' if os.name == 'nt' else 'clear')
            if move in move_list:

                new_position = self.move_down(self.current_position)
                self.clear_piece(self.current_position)
                if self.collision_check(self.current_coords, new_position):
                    self.display_piece(new_position)
                    self.current_position = new_position 
                        
                    if move in ['a', 'd']: #side-ways
                        side_position = self.move_sideways(new_position, move_list[move])
                        self.clear_piece(new_position)
                        if self.collision_check(self.current_coords, side_position):
                            self.display_piece(side_position)
                            self.current_position = side_position
                        else:
                            self.display_piece(new_position)

                    elif move == 'z' or move == 'x': #rotation
                        self.clear_piece(self.current_position)
                        rotate_coords = self.pieces.rotate(self.current_piece, self.current_coords, move_list[move])
                        if self.collision_check(rotate_coords, self.current_position):
                            self.current_coords = rotate_coords
                            self.display_piece(self.current_position)
                        else:
                            self.display_piece(self.current_position)

                    elif move == ' ': #hard-drop
                        while True:
                            new_position = self.move_down(self.current_position)
                            self.clear_piece(self.current_position)
                            if self.collision_check(self.current_coords, new_position):
                                self.display_piece(new_position)
                                self.current_position = new_position 
                            else:
                                self.display_piece(self.current_position)

                                bag_int += 1
                                self.garbage_collector()
                                if bag_int < 10:
                                    self.spawn_piece(bags[bag_int])
                                    self.display_piece(self.current_position)
                                else:
                                    bags = self.pieces.random_bag()
                                    bag_int = 0
                                    self.spawn_piece(bags[bag_int])
                                    if self.game_over():
                                        break
                                    self.display_piece(self.current_position)
                                break

                else:
                    self.display_piece(self.current_position)

                    bag_int += 1
                    self.garbage_collector()
                    if bag_int < 10:
                        self.spawn_piece(bags[bag_int])
                        if self.game_over():
                            break
                        self.display_piece(self.current_position)
                    else:
                        bags = self.pieces.random_bag()
                        bag_int = 0
                        self.spawn_piece(bags[bag_int])
                        if self.game_over():
                            break
                        self.display_piece(self.current_position)

                self.display_board()
            else:
                new_position = self.move_down(self.current_position)
                self.clear_piece(self.current_position)
                if self.collision_check(self.current_coords, new_position):
                    self.display_piece(new_position)
                    self.current_position = new_position
                else:
                    self.display_piece(self.current_position)
                    bag_int += 1
                    self.garbage_collector()
                    if bag_int < 10:
                        self.spawn_piece(bags[bag_int])
                        if self.game_over():
                            break
                        self.display_piece(self.current_position)
                    else:
                        bags = self.pieces.random_bag()
                        bag_int = 0
                        self.spawn_piece(bags[bag_int])
                        if self.game_over():
                            break
                        self.display_piece(self.current_position)

                self.display_board()
                continue

game = Board()
game.play()
