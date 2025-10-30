from curses import wrapper
import random 

def main(stdscr):
    stdscr.clear()
    state = 0
    counter = 0
    state_list = ['running', 'stopped']
    integer = random.randint(0, 10000)

    while True:
        move = stdscr.getch()

        if move == ord('q'):
            exit()
        elif move == ord('r'):
            counter += 1
            integer = random.randint(0, 10000)
        elif move == ord('s'):
            counter += 1
            state = 1 - state
        elif move == ord('c'):
            counter = 0

        stdscr.clear()
        stdscr.addstr(5, 10, f"random Number: {integer}")
        stdscr.addstr(10, 10, f"status: {state_list[state]}")
        stdscr.addstr(15, 10, f"counter: {counter}")
        stdscr.addstr(25, 10, f"last key pressed: {chr(move) if 32 <= move <= 126 else move}")
        stdscr.refresh()

wrapper(main)
        
