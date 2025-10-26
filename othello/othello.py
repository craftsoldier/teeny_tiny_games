class Board:
    def __init__(self):
        self.height = 8
        self.width = 8
        self.players = ['B', 'W']
        self.board = [[None] * self.width for i in range(self.height)]
        self.direction_list = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.board[3][3] = self.players[1]  # W at D4
        self.board[4][4] = self.players[1]  # W at E5
        self.board[3][4] = self.players[0]  # B at E4
        self.board[4][3] = self.players[0]  # B at D5

    def check_coord(self, coord, player):
        x, y = coord[0], coord[1]
        if not ((0 <= x < self.height) and (0 <= y < self.width)):
            return False
        return self.board[x][y] == self.players[player]

    def flip_sequence(self, start, direction, end, player):
        x, y = start[0] + direction[0], start[1] + direction[1]
        while (x, y) != end:
            self.board[x][y] = self.players[player]
            x += direction[0]
            y += direction[1]

    @property
    def board_full(self):
        for i in range(self.height):
            for k in range(self.width):
                if self.board[i][k] is None:
                    return False
        return True

    def check_winner(self):
        white_count = 0
        black_count = 0
        for i in range(self.height):
            for k in range(self.width):
                if self.board[i][k] == self.players[0]:
                    black_count += 1
                elif self.board[i][k] == self.players[1]:
                    white_count += 1

        if white_count > black_count:
            return 1
        elif black_count > white_count:
            return 0
        else:
            return None

    def has_valid_moves(self, player):
        for i in range(self.height):
            for k in range(self.width):
                if self.board[i][k] is None:
                    if self.check_sequence_flippable((i, k), player):
                        return True
        return False

    def check_sequence_flippable(self, move, player):
        x = move[0]
        y = move[1]
        flippable = []
        for direction in self.direction_list:
            search_coord_x, search_coord_y = x + direction[0], y + direction[1]

            if self.check_coord((search_coord_x, search_coord_y), 1 - player):
                search_coord_x, search_coord_y = search_coord_x + direction[0], search_coord_y + direction[1]

                while True:
                    if self.check_coord((search_coord_x, search_coord_y), 1 - player):
                        search_coord_x, search_coord_y = search_coord_x + direction[0], search_coord_y + direction[1]
                    elif self.check_coord((search_coord_x, search_coord_y), player):
                        flippable.append((direction, (search_coord_x, search_coord_y)))
                        break
                    else:
                        break
        if len(flippable) == 0:
            return False
        else:
            return flippable

    def get_score(self):
        black_count = 0
        white_count = 0
        for i in range(self.height):
            for k in range(self.width):
                if self.board[i][k] == self.players[0]:
                    black_count += 1
                elif self.board[i][k] == self.players[1]:
                    white_count += 1
        return black_count, white_count

    def draw_board(self, current_player=None):
        if current_player is not None:
            black_score, white_score = self.get_score()
            print(f"\n{'='*35}")
            print(f"turn: {self.players[current_player]} | black: {black_score} | white: {white_score}")
            print(f"{'='*35}")

        print("\n   ", end='')
        for col in range(self.width):
            print(f" {chr(65 + col)}", end='')
        print()

        print("   ┌", end='')
        for col in range(self.width * 2 + 1):
            print("─", end='')
        print("┐")

        for i in range(self.height):
            print(f" {i + 1} │ ", end='')
            for k in range(self.width):
                if self.board[i][k] is None:
                    print('·', end=' ')
                else:
                    print(self.board[i][k], end=' ')
            print("│")

        print("   └", end='')
        for col in range(self.width * 2 + 1):
            print("─", end='')
        print("┘")

class Game:
    def __init__(self):
        self.othello = Board()

    def get_move(self, player):
        try:
            move = input(f"player {self.othello.players[player]}, enter move (e.g. D3): ")
            if not move or len(move) < 2:
                raise ValueError("invalid input")
            y = ord(move[0].upper()) - ord('A')
            x = int(move[1:]) - 1
            if not (0 <= x < self.othello.height and 0 <= y < self.othello.width):
                raise ValueError("out of bounds")
            return (x, y)
        except KeyboardInterrupt:
            raise
        except (EOFError, SystemExit):
            print("\nexiting game...")
            raise
        except:
            print("invalid input! use format like 'D3' (column A-H, row 1-8)")
            return self.get_move(player)

    def play(self):
        board = self.othello
        player = 0
        consecutive_passes = 0

        while True:
            if board.board_full:
                board.draw_board()
                print("game over - board is full")
                black_score, white_score = board.get_score()
                print(f"black: {black_score}, white: {white_score}")
                winner = board.check_winner()
                if winner is not None:
                    print(f"player {board.players[winner]} wins!")
                else:
                    print("game draws")
                break

            if not board.has_valid_moves(player):
                board.draw_board(current_player=player)
                print(f"no valid moves for {board.players[player]}, passing...")
                player = 1 - player
                consecutive_passes += 1

                if consecutive_passes >= 2:
                    board.draw_board()
                    print("game over - no valid moves for either player")
                    black_score, white_score = board.get_score()
                    print(f"black: {black_score}, white: {white_score}")
                    winner = board.check_winner()
                    if winner is not None:
                        print(f"player {board.players[winner]} wins!")
                    else:
                        print("game draws")
                    break
                continue

            board.draw_board(current_player=player)
            move = self.get_move(player)
            check_sequence = board.check_sequence_flippable(move, player)

            if check_sequence and board.board[move[0]][move[1]] is None:
                consecutive_passes = 0
                board.board[move[0]][move[1]] = board.players[player]
                for direction, endpoint in check_sequence:
                    board.flip_sequence(move, direction, endpoint, player)

                player = 1 - player
            else:
                if board.board[move[0]][move[1]] is not None:
                    print(f"invalid move: square is already occupied. try again.")
                else:
                    print(f"invalid move: this move doesn't flip any pieces. try again.")

if __name__ == "__main__":
    game = Game()
    try:
        game.play()
    except (KeyboardInterrupt, EOFError):
        print("\ngame ended")
