from deck import Deck
from player import Player
new_deck = Deck()
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]
print(first_card, last_card)

# for i,card in enumerate(new_deck.all_cards):
#    print(f"Crd Number {i} is {card}")

new_deck.shuffle_card()
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]
print(first_card, last_card)
length = len(new_deck.all_cards)
print(length)
deal_card = new_deck.deal_on()

#while length <= 52:
#    deal_card = new_deck.deal_on()
#    print(f"deal card is# {deal_card}")
#    print(f"total card#  {len(new_deck.all_cards)}")
#    if len(new_deck.all_cards) == 0:
#        break

ibrahim = Player('Ibrahim')
ibrahim.add_cards(deal_card)
print(ibrahim)
print(ibrahim.drop_card())
ibrahim.add_cards([deal_card,deal_card,deal_card,deal_card])
print(ibrahim)
ibrahim.drop_card()
print(ibrahim)