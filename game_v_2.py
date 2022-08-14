from deck import Deck
from hand import Hand
from chip import Chips
import common

print("WELCOME TO BLACKJACK GAME")
# start new deck card and shuffle it for 3 times
new_deck = Deck()
new_deck.shuffle_card()
new_deck.shuffle_card()
new_deck.shuffle_card()

# init Player Hand
player_hand = Hand()
player_hand.add_card(new_deck.deal_on())
player_hand.add_card(new_deck.deal_on())

# init Dealer's Hand
dealer_hand = Hand()
dealer_hand.add_card(new_deck.deal_on())
dealer_hand.add_card(new_deck.deal_on())

# set ep player's chips
player_chips = Chips()

# take player's bet
common.take_bit(player_chips)

# show some cards
common.show_some(player_hand, dealer_hand)

# start game
playing = True
while playing:
    # prompt to player for hit or s
    common.hint_or_stand(new_deck, player_hand)

    # show cards(but keep the first dealer's card hidden
    common.show_some(player_hand, dealer_hand)

    # if player hand exceeds 21
    if player_hand.value > 21:
        common.player_busts(player_hand, dealer_hand, player_chips)
        break

    # if player has not busts , play dealer until reach 17 this real rules for blackjack game
    if player_hand.value <= 21:
        while dealer_hand.value <= 17:
            common.hit(new_deck, dealer_hand)

    # show all cards
    common.show_all(player_hand, dealer_hand)

    # show win scenario
    if dealer_hand.value > 21:
        common.dealer_busts(player_hand, dealer_hand, player_chips)
    elif dealer_hand.value > player_hand.value:
        common.dealer_win(player_hand, dealer_hand, player_chips)
    elif dealer_hand.value < player_hand.value:
        common.player_win(player_hand, dealer_hand, player_chips)
    else:
        common.push(player_hand, dealer_hand)

    # show total chip
    print(f"\n Player's total chips is# {player_chips.total}")

    # ask play gain
    x = input("Do you want play again? [y/n] ")
    if x[0].lower() == 'y':
        continue
    else:
        print("thanks you for playing!!! ")
        playing = False
