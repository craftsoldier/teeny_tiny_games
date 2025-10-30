class Game:
    def __init__(self):
        self.deck = { 'A': 11, 
                      'J': 10, 
                      'Q': 10, 
                      'K': 10, 
                      '10': 10, 
                      '9': 9, 
                      '8': 8, 
                      '7': 7, 
                      '6': 6, 
                      '5': 5, 
                      '4': 4,
                      '3': 3, 
                      '2': 2, 
                      '1': 1}
        self.deck_list = ['A', 'J', 'K', 'Q', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']

    def get_move(self):
        move = input()
        if move in self.deck_list:
            return self.deck[move]

    def

    def play():


