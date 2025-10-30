from curses import wrapper

def main(stdscr):
    stdscr.clear()
    x, y = stdscr.getmaxyx()
    stdscr.addstr(5, 10, "hello world")
    for i, k in zip(range(x), range(y)):
        stdscr.addstr(i, k, "hello world")
    stdscr.refresh()
    stdscr.timeout(1000)
    move = stdscr.getch()
    if move == ord('q'):
        exit()


wrapper(main)

