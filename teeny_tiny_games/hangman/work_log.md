# Hangman Project - Work Log

**Project Start:** 3:04pm
**Deadline:** 4:00pm
**Time Available:** 56 minutes

---

## Tasks

### [3:04pm] Project Setup
- Created work log
- Directory initialized
- **Status:** Complete
- **Duration:** <1 min

### [3:04pm] Learning Hangman Rules
- Reading and understanding game mechanics
- **Status:** Complete
- **Duration:** ~2 min

### [3:06pm] Design Phase
- Discussed Heaton's approach for hangman
- Broke down core components (6 functions identified)
- Decided on simplified version (no ASCII drawing)
- **Status:** Complete
- **Duration:** ~2 min

### [3:08pm] Code Status Check
- **hangman.py:** Does not exist yet
- **Next step:** Create file and start coding
- **Status:** Ready to code

---

### [3:08pm - 3:20pm] Initial Coding Session
- Created hangman.py
- Built `word_generator()` function - picks word from list ✅
- Started `display_word()` function - IN PROGRESS (syntax error on line 13)
- Started `play()` game loop - IN PROGRESS
- **Status:** Coding in progress
- **Duration:** ~12 minutes

---

### [3:20pm - 3:30pm] Core Development & Debugging
- Fixed syntax errors:
  - Added `import random` ✅
  - Fixed `range(len(word))` ✅
- Completed `display_word()` function ✅
- Built `check_win()` function with None handling ✅
- Implemented game loop with:
  - 6 wrong guesses limit ✅
  - Correct/incorrect guess logic ✅
  - Win condition checking ✅
- **Status:** Near completion
- **Duration:** ~10 minutes

---

### [3:30pm - 3:55pm] Final Polish & Bug Fixes
- Added `if __name__ == "__main__":` to run game ✅
- Fixed display formatting (added newline) ✅
- Added case-insensitivity with `.lower()` ✅
- Added single character validation `len(guess) == 1` ✅
- Added wrong guess counter feedback ✅
- Added "YOU LOST" message ✅
- **Status:** COMPLETE
- **Duration:** ~25 minutes

---

## FINAL STATE (3:55pm) ✅
- **Deadline:** 4:00pm
- **Completion Time:** 3:55pm
- **TIME SAVED:** 5 minutes early! 🔥
- **Total Code:** 55 lines
- **Functions Built:** 4 (word_generator, display_word, check_win, main)
- **Game Status:** ✅ FULLY FUNCTIONAL

### Features Implemented:
✅ Random word selection
✅ Hidden word display with underscores
✅ Letter guessing with validation
✅ Case-insensitive input
✅ Single character validation
✅ Win/loss detection
✅ 6 wrong guess limit
✅ Guess counter feedback
✅ Win/loss messages

### Known Limitations (acceptable for v1.0):
- No tracking of previously guessed letters (repeat guesses penalized)
- Small word list (3 words)

## PROJECT COMPLETE! 🎉

---

### [4:00pm - 4:15pm] Vocabulary Expansion
- Researched word list sources online ✅
- Downloaded words.txt from GitHub (853 words) ✅
- Implemented file reading with `.read().split('\n')` ✅
- Refactored `word_generator()` to read from file ✅
- Fixed bugs:
  - Line 5: `randint()` syntax fixed ✅
  - Line 34: Removed undefined `number` parameter ✅
- **Status:** COMPLETE & TESTED
- **Duration:** ~15 minutes

---

## FINAL STATS (4:15pm)
- **Total Project Time:** ~70 minutes (3:04pm - 4:15pm)
- **Original Deadline:** 4:00pm
- **Actual Completion:** 3:55pm (v1.0), 4:15pm (v1.1 with expanded vocab)
- **Lines of Code:** 55
- **Vocabulary Size:** 853 words (up from 3!)
- **Status:** ✅ FULLY FUNCTIONAL with expanded word list

## Skills Learned:
✅ Game logic design & implementation
✅ Input validation
✅ Win/loss condition handling
✅ File I/O (reading from .txt files)
✅ Random selection from lists
✅ Debugging syntax & logic errors
✅ String manipulation & list comprehensions

---
