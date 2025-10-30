from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.timeout(50)

    while True:
        stdscr.clear()

        # Get terminal dimensions
        y, x = stdscr.getmaxyx()

        # Create display strings
        dimensions_text = f"Terminal Size: {y} rows x {x} cols"

        # Calculate center positions
        center_y = y // 2
        center_x = (x - len(dimensions_text)) // 2

        # Display in center
        stdscr.addstr(center_y, center_x, dimensions_text)
        stdscr.addstr(center_y + 2, (x - 17) // 2, "Press 'q' to quit")

        stdscr.refresh()

        move = stdscr.getch()
        if move == ord('q'):
            exit()

wrapper(main)
