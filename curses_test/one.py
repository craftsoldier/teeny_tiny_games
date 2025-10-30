from curses import wrapper

def main(stdscr):
    stdscr.clear()

    y, x = stdscr.getmaxyx()
    position_x, position_y = 5, 10
    hit_edge = 1
    hit_ceiling = 1
    stdscr.timeout(50)
    while True:
        stdscr.erase()
        stdscr.addstr(position_y, position_x, 'HELLO')
        stdscr.refresh()

        if position_x > x - 10:
            hit_edge = -1
        elif position_x < 5:
            hit_edge = 1

        if position_y > y - 20:
            hit_ceiling = -1
        elif position_y < 20: 
            hit_ceiling = 1

        position_x += hit_edge
        position_y += hit_ceiling

        move = stdscr.getch()
        if move == ord('q'):
            exit()
     

wrapper(main)
