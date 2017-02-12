from random import shuffle

class Deck:
    cards = []
    
    def __init__(self):
        rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suit = ['C','S','D','H']
        self.cards = self.cartesian_product(rank,suit)
        shuffle(self.cards)
        

    def cartesian_product(self,list_1,list_2):
        product = []
        for item in list_1:
            for thing in list_2:
                product.append("{}{}".format(item,thing))
        return product

    
    def go_fish(self):
        return self.cards.pop()


    def deal_hands(self):
        hand_1 = self.cards[0:7]
        hand_2 = self.cards[7:14]
        del self.cards[:14]
        return hand_1,hand_2
        
