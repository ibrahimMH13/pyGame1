from gameElement import GameElement


class Hand(GameElement):

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += self.VALUES[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace(self):

        # check if value in player hand greater than 21
        # change my aces card to be a 1 ace card instead of an 11 (11 is range of ace card in constant )
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
