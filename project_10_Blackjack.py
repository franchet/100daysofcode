# Blackjack in Python
# by @iAmFranchet

import random
# Game Logic
# Create Deck of Cards
# Dealer Cards
# Player Cards
# # Deal the cards
# Display the cards
# Player Cards
# Sum of the Dealer cards
# Sum of the Player Cards
# Compare the sums of the cards between Dealer and Player
# If Player card sum is greater than 21 = BUST!
# If Player card sum is less than 21 = Option Hit or Stay
# If P option = Stay ... Compare sum of Dealer and Player cards
# If Player sum < 21 and > Dealer sum then Player Wins!
# If Player sum < Dealer sum then P loses!


print("Welcome to Blackjack!")

dealer_cards = []

player_cards = []


while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has: x & ", dealer_cards[1])


while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have: ", player_cards)


if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")


while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit? "))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " +
              str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " +
              str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " +
              str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer Wins!")
        else:
            print("You Win")
            break

if sum(player_cards) > 21:
    print("You BUSTED! Dealer wins.")
elif sum(player_cards) == 21:
    print("You have a BLACKJACK! You win!!! 21")
