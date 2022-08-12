import gameElement


class Card(gameElement.GameElement):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.VALUES[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


two_hearts = Card('hearts', 'Two')
three_clubs = Card("clubs", "Three")
