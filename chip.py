class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_a_bit(self):
        self.total += self.bet

    def lose_a_bit(self):
        self.total -= self.bet

