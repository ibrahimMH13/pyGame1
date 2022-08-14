def take_bit(chips):
    while True:

        try:
            enter_chips = int(input('Enter your Chips Value ? '))
        except:
            print("Sorry , Wrong value must enter a valid number please!!! ")
        else:
            if enter_chips > chips.total:
                print(
                    f"Sorry , you do not have enough value , you are have {chips.total} only,please renter again# ")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal_on())
    hand.adjust_ace()


def hint_or_stand(deck, hand):
    global playing
    while True:
        x = input('to choose Hint or Stand Enter [H] OR [S]# ?')

        if x[0].upper() == 'H':
            hit(deck, hand)

        elif x[0].upper() == 'S':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry, i cannot understand that !!!,plase enter H OR S")
            continue
        break


def show_some(player, dealer):
    # HERE will show 2end one card not the first
    # show only one of dealer's card
    print("\n Dealer's Hand:")
    print("First Card Hidden !!")
    print(dealer.cards[1])

    # show all (2 card) of player's (hand/card)
    print("\n Player's Hand:")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    pass
    # show all dealer's card
    #    print("\n Dealer's Hand:")
    #    for card in dealer.cards:
    #        print(card)
    #   other way for print loop is use *
    print("\n Dealer's Hand:", *dealer.cards, sep="\n")  # use this for print through loop
    # calculate and display value LIKE THIS (J + K =20)
    print(f"Value of Dealer Hand is: {dealer.value}")
    # show all player's card
    print("\n Player's Hand:")
    for card in player.cards:
        print(card)
    print(f"Value of Dealer Hand is: {player.value}")


def player_busts(player, dealer, chips):
    print("BUSTS Player ")
    chips.lose_a_bit()


def player_win(player, dealer, chips):
    print("Player Win ")
    chips.win_a_bit()


def dealer_busts(player, dealer, chips):
    print("Player Win, Dealer BUSTED ")
    chips.win_a_bit()


def dealer_win(player, dealer, chips):
    print("Dealer Win ")
    chips.lose_a_bit()


def push(player, dealer):
    print("Dealer and player tie, PUSH!!")
