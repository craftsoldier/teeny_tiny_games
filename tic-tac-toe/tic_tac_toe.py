import os

def draw_board(board):
    os.system('clear')
    for row in board:
        row_display = ""
        for cell in row:
            if cell is None:
                row_display += ". "
            else:
                row_display += cell + " "
        print(row_display)

def new_board():
    board = [[None, None, None], [None, None, None], [None, None, None]]
    draw_board(board)
    return board

def get_move():
    number = int(input("Pick a spot on the board"))
    return number

def make_move(board, position, player):
    row = (position - 1) // 3
    column = (position - 1) % 3
    if board[row][column] not in ['X', 'O']:
        board[row][column] = player
    else:
        return False
    return True

def check_winner(board):
    win_list = [[(0,0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]

    for win in win_list:
        x_win = True
        o_win = True
        for j, k in win:
            if board[j][k] == 'O':
                x_win = False
            elif board[j][k] == 'X':
                o_win = False
            elif board[j][k] == None:
                x_win = False
                o_win = False
        if x_win:
            return True
        elif o_win:
            return True
    return False

def is_board_full(board):
    is_board_full = True
    for i in range(3):
        for k in range(3):
            if board[i][k] != 'X' and  board[i][k] != 'O':
                is_board_full = False
    return is_board_full

def switch_player(player):
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
    return player
    

def main():
    board = new_board()
    current_player = 'X'

    while not is_board_full(board):
        while True:
            player = get_move() 
            if make_move(board, player, current_player):
                break
            else:
                continue

        if not check_winner(board):
            draw_board(board)
        elif check_winner(board):
            draw_board(board)
            print(f"{current_player} WINS")
            break

        current_player = switch_player(current_player)

        if is_board_full(board):
            break

    if is_board_full(board) and not check_winner(board):
        print("draw")

if __name__ == "__main__":
    main()

