#AUTHOR: TIM STEVENS
from random import shuffle

#This class creates a deck of 52 cards  with 13 ranks and deals out hands of
#seven cards to each player
class Deck:
    cards = []

    #create a deck and shuffle it
    def __init__(self):
        rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = self.cartesian_product(rank)
        shuffle(self.cards)
        
    #make sure that there are 4 of each rank in the deck
    def cartesian_product(self,list_1):
        product = []
        for item in list_1:
            for thing in range(4):
                product.append(item)
        return product

    # deal hands to each player and pass the rest of the deck as an array
    def deal_hands(self):
        hand_1 = self.cards[0:7]
        hand_2 = self.cards[7:14]
        del self.cards[:14]
        return hand_1,hand_2,self.cards

        
