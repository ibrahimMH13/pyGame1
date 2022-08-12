from deck import Deck

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
while length <= 52:
    deal_card = new_deck.deal_on()
    print(f"deal card is# {deal_card}")
    print(f"total card#  {len(new_deck.all_cards)}")
    if len(new_deck.all_cards) == 0:
        break
