class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


two_hearts = Card('hearts', 'Two')
print(two_hearts)

values = {'Two': 2, 'Three': 3, 'four': 4,
          'five': 5, 'six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9,'Ten': 10,
          'Jak': 11,'Queen': 12, 'King': 13, 'Ace': 14}
