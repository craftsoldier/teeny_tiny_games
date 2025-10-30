  Project 1: The Bouncing Text

  What you'll learn: Positioning, loops, clearing, refresh timing

  Make text move across the screen (like DVD logo). Text starts at position (5, 10) and moves right by 1 each iteration.
  When it hits the edge, bounce back. Press 'q' to quit.

  Skills: timeout(), getch(), getmaxyx() to detect screen edges, coordinate system

  Project 2: Multi-Line Status Display

  What you'll learn: Organizing multiple pieces of information

  Display 5-6 lines of different "fake" stats that update:
  - Line 1: Current counter (increments each second)
  - Line 2: Random number that changes
  - Line 3: Static label
  - Line 4: Current time
  - Line 5: "Press q to quit"

  Skills: Multiple addstr() calls, formatted strings, layout planning

  Project 3: Color-Coded Status Board

  What you'll learn: Colors and attributes

  Show a status display with:
  - Green text for "CONNECTED"
  - Red text for "ERROR"
  - Yellow text for "WARNING"
  - Bold text for headings
  - Normal text for values

  Skills: init_pair(), color_pair(), A_BOLD, A_REVERSE

  Project 4: Terminal Size Detective

  What you'll learn: Responsive design

  Display the current terminal dimensions (rows, cols) in the center of the screen. When you resize the terminal, the
  display should re-center automatically.

  Skills: getmaxyx(), calculating center positions, handling dynamic layouts

  Project 5: Multi-Key Input Handler

  What you'll learn: Advanced keyboard input

  Build a menu where:
  - 'r' refreshes/updates something
  - 's' toggles between two states (like "Running"/"Stopped")
  - 'c' clears a counter
  - 'q' quits
  - Display what key was last pressed

  Skills: Checking different key values with ord(), state management

  Project 6: Mini Progress Monitor

  What you'll learn: Putting it all together

  Simulate a download progress:
  - Progress bar (using characters like █ and ░)
  - Percentage complete
  - Elapsed time
  - Speed indicator
  - Status messages

