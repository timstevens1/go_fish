print("Welcome to Go Fish: the computer program! you can play go fish against a computer program here based on 3 different difficulty level.")
print("Simple: The computer plays randomly.")
print("Strategic: The computer plays with some strategy.")
print("Deviant: The computer lies.")
print("That's about it for now folks. Good luck!")

player_1,player_2 = deck.deal_hands()
def select_difficulty():
    difficulty = 1


class Deck:

    cards = []
    def _init_(self):
        rank = [A,2,3,4,5,6,7,8,9,10,J,Q,K]
        suit = [C,S,D,H]
        cards = cartesian_product(self,rank,suit)
        cards = random.shuffle(cards)



    def cartesian_product(self,list_1,list_2):
        product = []
        for item in list_1:
            for thing in list_2:
                product.append("{}{}".format(item,thing))
        return product

    def go_fish(self):
        return cards.pop()

    def deal_hands():
        hand_1 = cards[0:7]
        hand_2 = cards[7:14]
        del cards[:14]
        return hand_1,hand_2
        
        

