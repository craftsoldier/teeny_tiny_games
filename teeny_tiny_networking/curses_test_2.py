import curses

def main(stdscr):
    stdscr.clear()

    y, x = 5, 10

    stdscr.addstr(y, x, "Hello, Curses!")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
