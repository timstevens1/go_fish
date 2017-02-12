from deck import Deck
import re
# input player hand and player counter
# output player hand with no decks and counter incremented to number of decks
def make_books(player, counter):
    # index of rank array is a mapping to num_decks
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # counters of number of cards of a given rank in the hand
    num_decks = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in player:
        # increments appropriate rank counter for each card
        num_decks[ranks.index(card[:-1])] +=1
    for i in range(12):
        # 4 cards of a rank in the hand
        if num_decks[i]>= 4:
            # increment deck counter
            counter+=1
            # remove deck from hand
            player = [x for x in player if not ranks[i] in x]
    return player, counter

    
# initialization statements
print("Welcome to Go Fish: the computer program! you can play go fish against a computer program here based on 3 different difficulty level.")
print("Simple: The computer plays randomly.")
print("Strategic: The computer plays with some strategy.")
print("Deviant: The computer lies.")
print("That's about it for now folks. Good luck!")
# initialize deck
deck = Deck()
#create hands
player_1, player_2 = deck.deal_hands()
counter_1, counter_2 = 0,0
# counter is number of decks
#the human player goes first human is player_1
