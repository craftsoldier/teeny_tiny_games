from curses import wrapper

def main(stdscr):
    counter = 0
    stdscr.timeout(1000)

    while counter < 110:
        stdscr.addstr(5, counter+11, "░")
        stdscr.addstr(5, counter+10, "█")
        stdscr.addstr(10, 10, f"download in progress {counter}% complete")
        seconds = (100 - counter) % 60
        minutes = (100 - counter) // 60
        stdscr.addstr(11, 10, f"time left: {minutes} minutes and {seconds} seconds")
        counter += 1
        if counter = 100:
            exit()
        move = stdscr.getch()
        if move == ord('q'):
            exit()
        stdscr.refresh()

wrapper(main)

