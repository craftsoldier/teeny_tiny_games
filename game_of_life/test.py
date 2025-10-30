from game import Game

if __name__ == "__main__":
    # Set up the test
    game = Game()
    game.width = 3
    game.height = 3
    game.board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    # Run the function
    game.next_state()

    # Check if it matches what we expect
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    if game.board == expected:
        print("Test passed!")
    else:
        print("Test failed!")
        print(f"Expected: {expected}")
        print(f"Got: {game.board}")

