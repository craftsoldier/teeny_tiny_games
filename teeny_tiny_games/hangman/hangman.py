import random

def word_generator():
    word_list = open('words.txt').read().split('\n')
    number = random.randint(0, len(word_list) - 1)
    word = word_list[number]
    return word


def display_word(word, dashes = None, letter = None):
    if dashes == None:
        dashes = ['_' for letter in word]
    for l in range(len(word)):
        if letter == word[l]:
            dashes[l] = letter
    for dash in dashes:
        print(dash, end = ' ')
    print()
    return dashes

def check_win(word, dashes = None):
    game_won = True
    if dashes != None:
        for i in range(len(word)):
            if word[i] != dashes[i]:
                game_won = False
    elif dashes == None:
        game_won = False
    return game_won

def main():
    dashes = None
    letter = None
    word = word_generator()
    display_word(word, dashes, letter)
    incorrect = 0
    while incorrect < 6:
        guess = input("enter your guess:  ")
        guess = guess.lower()
        if guess in word and len(guess) == 1:
            dashes = display_word(word, dashes, guess)
        else:
            incorrect += 1
            print(f"Wrong {6 - incorrect}/6 guesses remaining")

        if check_win(word, dashes):
            print("YOU WON")
            break

    if not check_win(word,dashes):
        print("YOU LOST")
        
if __name__ == "__main__":
    main()
