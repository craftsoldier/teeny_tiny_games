from curses import wrapper
import time
import random

def main(stdstr):
    stdstr.clear()
    stdstr.refresh()
    stdstr.timeout(100) 
    counter = -1
    while True:
        stdstr.clear()
        counter += 1
        counter_string = str(counter)
        stdstr.addstr(5, 10, counter_string)
        random_number = str(random.randint(0, 1000000))
        time_display = str(time.ctime())
        stdstr.addstr(1, 10, random_number)
        stdstr.addstr(2, 10, 'static label')
        stdstr.addstr(3, 10, time_display)
        stdstr.addstr(4, 10, "press q to quit")
        stdstr.refresh()
        move = stdstr.getch()
        if move == ord('q'):
            exit()

wrapper(main)
