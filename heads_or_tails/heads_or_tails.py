import random

def main():
    score_count = 0
    while True:
        move = input("enter (H)eads or (T)ails:  ").upper()
        print()
        if move == 'H':
            move = 0
        elif move == 'T': 
            move = 1
        else:
            print("invalid input")
            continue
        toss = random.randint(0,1)
        if move == toss:
            print(f"that was right! - total score: {score_count}")
            score_count += 1
        elif move != toss:
            print(f"wrong guess - total score: {score_count}")

main()
