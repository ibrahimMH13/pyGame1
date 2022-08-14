from deck import Deck
from player import Player
from  hand import Hand
'''
#this just test each function
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


'''
# create player instance
player_one = Player('You')
player_two = Player('Computer')

# crate collection play card and shuffle them
new_deck = Deck()
new_deck.shuffle_card()
new_deck.shuffle_card()
new_deck.shuffle_card()

# divide the cards for players
test_hand = Hand()
test_hand.add_card(new_deck.deal_on())
test_hand.add_card(new_deck.deal_on())
test_hand.add_card(new_deck.deal_on())
print(test_hand.value)
print(test_hand.aces)
test_hand.adjust_ace()
print(test_hand.value)

'''

for x in range(26):
    player_one.add_cards(new_deck.deal_on())
    player_two.add_cards(new_deck.deal_on())

round_number = 0
game_one = True
while game_one:
    round_number += 1
    print(f"----------------| Round {round_number} |----------------")

    if len(player_one.list_cards) == 0:
        print("Player One,Out of Cards!!!, So Play Two Win!!!")
        game_one = False
        break

    if len(player_two.list_cards) == 0:
        print("Player Two,Out of Cards!!!, So Play Two Win!!!")
        game_one = False
        break

    player_one_cards = [player_one.drop_card()]
    player_two_cards = [player_two.drop_card()]

    at_war = True
    while at_war:
        player_one_card = player_one_cards[-1].value
        player_two_card = player_two_cards[-1].value
        print(f"Player One card {player_one_cards[-1]} >><< {player_two_cards[-1]} Player Two Card")
        if player_one_card > player_two_card:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_card < player_two_card:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('WAR!!!')
            if (len(player_one.list_cards)) < 5:
                print("Player One con not Declare  War")
                print("So Player Two Win !!! :)")

                game_one = False
                break
            elif (len(player_two.list_cards)) < 5:
                print("Player Two con not Declare  War")
                print("So Player One Win !!! :)")
                game_one = False
                break
            else:
                for r in range(5):
                    player_one.drop_card()
                    player_two.drop_card()
'''
