# teeny_tiny_games

A collection of classic games implemented in Python, designed to be played in the terminal.

## Games Collection

### Board Games

#### Battleships
A two-player naval warfare game on a 10x10 grid.

**Features:**
- Random ship placement (Carrier, Battleship, Cruiser, Submarine, Destroyer)
- Turn-based gameplay
- Shot tracking with hit/miss markers (H/M)
- Each ship has unique symbols: X (Carrier), # (Battleship), $ (Cruiser), @ (Submarine), 0 (Destroyer)
- Win condition: sink all 17 ship cells

**Controls:** Type coordinates (e.g., "A5")

**How to Play:**
- Players take turns entering shots (e.g., "A5")
- Hit markers (H) and miss markers (M) track progress
- First player to sink all enemy ships wins

---
#### Connect Four
Classic two-player connection game on a 6x7 grid.

**Features:**
- Colored pieces (white and gray circles)
- Gravity-based piece dropping
- Win detection in all directions (horizontal, vertical, diagonal)
- Column validation

**Controls:** Type column number (1-7)

**How to Play:**
- Players alternate dropping pieces into columns (1-7)
- First player to connect 4 pieces in any direction wins
---

#### Othello (Reversi)
Strategic board game on an 8x8 grid where players flip opponent pieces.

**Features:**
- Standard Othello starting position
- Valid move detection with piece flipping
- Real-time score tracking (Black vs White)
- Automatic pass when no valid moves available
- Win/draw detection

**Controls:** Type position (e.g., "D3")

**How to Play:**
- Players alternate placing pieces (format: "D3")
- Flank opponent pieces to flip them to your color
- Player with most pieces when board fills or no moves remain wins

---
#### Tic-Tac-Toe
Classic 3x3 grid game for two players.

**Features:**
- Simple numbered position entry (1-9)
- Win detection for rows, columns, and diagonals
- Draw detection

**Controls:** Type position (1-9)

**How to Play:**
- Players alternate marking positions 1-9
- First to get 3 in a row wins

---
#### Snake
Classic snake game with growing mechanics.

**Features:**
- WASD movement controls
- Wrap-around board edges
- Apple collection for growth and scoring
- Collision detection with self
- Real-time score display

**Controls:** W (up), A (left), S (down), D (right)

**How to Play:**
- Control: W (up), A (left), S (down), D (right)
- Eat apples (A) to grow and score points
- Avoid running into yourself
---

#### Tetris
Full-featured Tetris implementation with standard pieces.

**Features:**
- All 7 standard tetrominos (I, J, L, O, S, Z, T)
- Rotation controls (Z/X for counter-clockwise/clockwise)
- Side movement (A/D)
- Hard drop (spacebar)
- Line clearing with garbage collection
- 20x10 playing field

**Controls:** A/D (move left/right), Z/X (rotate), Space (hard drop)

**How to Play:**
- A/D: Move left/right
- Z/X: Rotate counter-clockwise/clockwise
- Space: Hard drop
- Any other key: Soft drop (piece moves down one row)
- Clear lines by filling rows completely

---
#### Hangman
Classic word-guessing game with comprehensive word list.

**Features:**
- Large word database (`words.txt`)
- 6 incorrect guess limit
- Letter-by-letter reveal
- Win/loss detection

**Controls:** Type single letter

**How to Play:**
- Guess letters one at a time
- 6 wrong guesses allowed
- Guess all letters in the word to win

---
#### ASCII Art Converter
Converts images to ASCII art representation.

**Features:**
- Loads JPEG images using PIL (Pillow)
- Converts pixel brightness to ASCII characters
- 65-character gradient for detailed output
- Character set: `` `^",:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$ ``

**How to Use:**
- Place image file as `ascii.jpeg` in the ASCII directory
- Run script to generate ASCII art in terminal

---
## Notes

- Most games use `os.system('clear')` to refresh the display
- Battleships and Connect Four use ANSI color codes for enhanced visuals
- All games are terminal-based and require no GUI
- Some games support graceful exit with Ctrl+C

## Project Structure

```
games/
├── ASCII/          # Image to ASCII art converter
├── battleships/    # Naval warfare game
├── connect_four/   # Connection game
├── hangman/        # Word guessing game
├── othello/        # Strategic board game
├── snake_game/     # Classic snake
├── tetris/         # Falling blocks puzzle
├── tic-tac-toe/    # Classic 3x3 game
└── user_logins/    # (Authentication utilities)
```
