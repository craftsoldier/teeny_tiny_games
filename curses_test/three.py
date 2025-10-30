from curses import wrapper
import curses

def main(stdscr):
    stdscr.clear()

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.timeout(100)

    while True:
        stdscr.clear()

        # Bold headings with normal values
        stdscr.addstr(2, 10, "Connection Status: ", curses.A_BOLD)
        stdscr.addstr(2, 29, "CONNECTED", curses.color_pair(1))

        stdscr.addstr(4, 10, "Error Status: ", curses.A_BOLD)
        stdscr.addstr(4, 24, "ERROR", curses.color_pair(2))

        stdscr.addstr(6, 10, "Warning Status: ", curses.A_BOLD)
        stdscr.addstr(6, 26, "WARNING", curses.color_pair(3))

        stdscr.addstr(8, 10, "System Mode: ", curses.A_BOLD)
        stdscr.addstr(8, 23, "Active")

        stdscr.addstr(10, 10, "Server Health: ", curses.A_BOLD)
        stdscr.addstr(10, 25, "CONNECTED", curses.color_pair(1))

        stdscr.addstr(15, 10, "Press 'q' to quit", curses.A_REVERSE)

        stdscr.refresh()

        move = stdscr.getch()
        if move == ord('q'):
            exit()

wrapper(main)
