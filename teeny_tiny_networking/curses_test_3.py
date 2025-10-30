import curses

def main(stdscr):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    stdscr.addstr(5, 10, "running some program...")
    stdscr.refresh()

    teardown(stdscr)

def teardown(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

main()
