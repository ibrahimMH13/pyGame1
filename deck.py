import random
from gameElement import GameElement
from card import Card


class Deck(GameElement):

    def __init__(self):
        self.all_cards = []
        for suit in self.SUITES:
            for rank in self.RANKS:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_card(self):
        random.shuffle(self.all_cards)

    def deal_on(self):
        return self.all_cards.pop()