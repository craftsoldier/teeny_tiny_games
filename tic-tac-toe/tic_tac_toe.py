def draw_board(board):
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
    position = get_move()
    row = (position - 1) // 3
    column = (position - 1) % 3
    board[row][column] = player
    return board
    
def check_winner(board):
    winning_patterns = 

    


