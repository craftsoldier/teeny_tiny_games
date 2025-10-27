import os
import random

class Game:
    def __init__(self):
        self.beats = { 'R': 'S',
                       'P': 'R',
                       'S': 'P'}

        self.player_scores = [0, 0]
        self.valid_moves = ['R', 'P', 'S', 'Q']
        self.last_result = ""
        self.round_number = 0

    def game_ui(self, score_player=0, score_computer=0, last_result=""):
        print("\n╔═══════════════════════════════════════════════╗")
        print("║         Rock  •  Paper  •  Scissors           ║")
        print(f"║  Player: {score_player:<3}                 Computer: {score_computer:>3}    ║")
        print(f"║  Round: {self.round_number:<36}  ║")
        if last_result:
            print(f"║  Last Round: {last_result:<30}   ║")
        print("╠═══════════════════════════════════════════════╣")
        print("║                Make your move:                ║")
        print("║                                               ║")
        print("║                   (R)ock                      ║")
        print("║                   (P)aper                     ║")
        print("║                   (S)cissors                  ║")
        print("║                                               ║")
        print("║                   (Q)uit                      ║")
        print("╚═══════════════════════════════════════════════╝")

    def get_move(self):
        move = input("enter move...").upper()
        if move == 'Q':
            self.check_winner()
        elif move in self.valid_moves:
            return move
        else:
            print(f"\n'{move}' is not a valid move - enter R, P, S, or Q.")
            input("press enter to continue...")
            return self.get_move()

    def computer_move(self):
        ai_move = random.randint(0, 2)
        ai_move = self.valid_moves[ai_move]
        return ai_move

    def check_win(self, move_x, move_y):
        self.round_number += 1
        if move_x == move_y:
            self.last_result = f"tie!"
        elif self.beats[move_x] == move_y:
            self.player_scores[0] += 1
            self.last_result = f"player 1 won!"
        else:
            self.player_scores[1] += 1
            self.last_result = f"computer 2 won!"

    def check_winner(self):
        if self.player_scores[0] > self.player_scores[1]:
            print(f"player 1 wins the game!")
            exit()
        elif self.player_scores[0] < self.player_scores[1]:
            print(f"computer 2 wins the game!")
            exit()
        elif self.player_scores[0] == self.player_scores[1]:
            print(f"game ends at a draw")
            exit()
        
    def play(self):
        while True:
            os.system('clear')
            self.game_ui(self.player_scores[0], self.player_scores[1], self.last_result)
            self.check_win(self.get_move(), self.computer_move())

game = Game()
game.play()
