import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 10, 'running my program..')
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
