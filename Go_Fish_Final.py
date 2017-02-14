import random
from deck import Deck
import time
difficulty_level = input ("Welcome to Go Fish: the computer program! you can play go fish against a computer program here based on 3 different difficulty levels:\n"+
                          "1: The computer plays randomly.\n"+"2: The computer plays with some strategy.\n"+"3: The computer lies.\n")
PLAYER_HAND = []
COMPUTER_HAND = []
PLAYER_SCORE = 0
COMPUTER_SCORE = 0
LIES = 1
TOTAL_CARDS_PASSED = 0 # for stats
GF_COUNTER = 0
SUCCESS_COUNTER = 0
TIME_COUNTER = 0
TURN_COUNTER = 0
CARD_FREQUENCY = [0,0,0,0,0,0,0,0,0,0,0,0,0]
RANK = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

deck = Deck()
PLAYER_HAND, COMPUTER_HAND, deck = deck.deal_hands()
def Computer_Response(hand, level, card):
    global LIES
    response = False
    if level == "1":
        if card in hand:
            response = True
        return response
        #computer chooses card to ask for at random from cards in its hand
        
    if level == "2":
        if card in hand:
            response = True
        return response
        #computer asks for card drawn or rotates through other cards

    if level == "3":
        if card in hand and LIES != 3:
            response = True
            LIES += 1
        if card in hand and LIES == 3:
            response = False
            LIES = 1
        return response
          
        #computer lies every 3rd time it has what player asks for
    



# adds correct number of cards to hand that asked for them
def add_cards(hand,card,num):
    x = 0
    while x < num:
        hand.append(card)
        x += 1
    return hand
    
#removes the correct number of cards from the hand that had them
def remove_cards(hand,card,num):
    x = 0
    while x < num:
        hand.remove(card)
        x += 1
    return hand

#gets the number of cards of the type asked for from the asked hand
def num_cards_of_type_asked(hand,card):
    global TOTAL_CARDS_PASSED
    global RANK
    global CARD_FREQUENCY
    num_cards = 0
    for x in hand:
        if x==card:
            num_cards+=1
    TOTAL_CARDS_PASSED += num_cards
    CARD_FREQUENCY[RANK.index(card)] += num_cards
    return num_cards

#makes sure that the deck is not empty before they draw a card. 
def Go_Fish():
    global deck
    global GF_COUNTER
    deck_empty = False
    if len(deck) == 0:
        deck_empty = True
    else:
        print ("\nGo fish...\n")
        GF_COUNTER +=1
    return deck_empty


#determine if player has books of cards and tally score. 
def Make_Books(player, counter):
    # index of rank array is a mapping to num_decks
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # counters of number of cards of a given rank in the hand
    num_decks = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in player:
        # increments appropriate rank counter for each card
        num_decks[ranks.index(card)] +=1
    for i in range(13):
        # 4 cards of a rank in the hand
        if num_decks[i]>= 4:
            # increment deck counter
            counter+=1
            # remove deck from hand
            player = [x for x in player if not ranks[i] in x]
    return player, counter


#print statistics at the end of the game. 
def End_Game():
    global TOTAL_CARDS_PASSED
    global PLAYER_SCORE
    global COMPUTER_SCORE
    global GF_COUNTER
    global TIME_COUNTER
    global SUCCESS_COUNTER
    global TURN_COUNTER
    global CARD_FREQUENCY
    global RANK
    TIME_COUNTER = time.time() - TIME_COUNTER
    avg_card_passed = TOTAL_CARDS_PASSED/(TURN_COUNTER*2)
    most_common_card = RANK[CARD_FREQUENCY.index(max(CARD_FREQUENCY))]
    least_common_card = RANK[CARD_FREQUENCY.index(min(CARD_FREQUENCY))]

    #computer wins
    if COMPUTER_SCORE > PLAYER_SCORE:
        print('You lost!')
        print('Game Stats:\n')
        print('Your Score: {}'.format(PLAYER_SCORE))
        print('Computer Score: {}'.format(COMPUTER_SCORE))
        print('Total cards passed: {}'.format(TOTAL_CARDS_PASSED))
        print('Total times players went fish: {}'.format(GF_COUNTER))
        print('Total correct guesses: {}'.format(SUCCESS_COUNTER))
        print('Most common card asked for: {} occurred {} times'.format(most_common_card,max(CARD_FREQUENCY)))
        print('Least common card asked for: {} occurred {} times'.format(least_common_card,min(CARD_FREQUENCY)))
        print('Mean number of cards passed per turn: {0:.1f}'.format(avg_card_passed))
        print('Number of turns: {}'.format(TURN_COUNTER))
        print('Game duration: {0:.2f}'.format(TIME_COUNTER),"seconds")
    #player wins
    else:
        print('Congratulations! You won!')
        print('Game Stats:\n')
        print('Your Score: {}'.format(PLAYER_SCORE))
        print('Computer Score: {}'.format(COMPUTER_SCORE))
        print('Total cards passed: {}'.format(TOTAL_CARDS_PASSED))
        print('Total times players went fish: {}'.format(GF_COUNTER))
        print('Total correct guesses: {}'.format(SUCCESS_COUNTER))
        print('Most common card asked for: {} occurred {} times'.format(most_common_card, max(CARD_FREQUENCY)))
        print('Least common card asked for: {} occurred {} times'.format(least_common_card, min(CARD_FREQUENCY)))
        print('Mean number of cards passed per turn: {0:.1f}'.format(avg_card_passed))
        print('Number of turns: {}'.format(TURN_COUNTER))
        print('Game duration: {0:.2f}'.format(TIME_COUNTER),"seconds")

#the players turn
def Player_Turn():
    global PLAYER_SCORE
    global TIME_COUNTER
    global GF_COUNTER
    global SUCCESS_COUNTER
    global COMPUTER_SCORE
    print ("Score: \t Player: ",PLAYER_SCORE,"Computer: ",COMPUTER_SCORE)
    global COMPUTER_HAND
    global PLAYER_HAND
    global deck
    TIME_COUNTER = time.time()
    #Handles case if player's hand is empty and the deck is not
    if len(PLAYER_HAND) == 0  and len(deck) !=0 :
        drawn_card = deck[random.randint(0,len(deck)-1)]
        PLAYER_HAND.append(drawn_card)
        deck.remove(drawn_card)
    #if players hand is not empty.
    elif len(PLAYER_HAND) !=0:
        PLAYER_HAND.sort()
        print("YOUR HAND: ",PLAYER_HAND,"\n")
        card = input ("What do you ask for? ")
        response = Computer_Response(COMPUTER_HAND, difficulty_level, card) # function to determine computer response
        #if computer has what the player asked for pass the cards
        if response == True:
            SUCCESS_COUNTER +=1
            print("You got what you asked for!\n")
            num_cards = num_cards_of_type_asked(COMPUTER_HAND,card)
            PLAYER_HAND = add_cards(PLAYER_HAND,card,num_cards)
            COMPUTER_HAND = remove_cards(COMPUTER_HAND,card,num_cards)
            PLAYER_HAND, PLAYER_SCORE = Make_Books(PLAYER_HAND,PLAYER_SCORE)
            PLAYER_HAND.sort()
            print ("YOUR HAND: ",PLAYER_HAND,"\n")
        #if computer does not have what the player asked for
        else:
            if not Go_Fish():#checks if there are cards in the deck to draw
                drawn_card = deck[random.randint(0,len(deck)-1)]
                PLAYER_HAND.append(drawn_card)
                deck.remove(drawn_card)
                print("You drew a ",drawn_card,"\n")
                #if player draws what they asked for. 
                if drawn_card == card:
                    card_2 = input ("You drew what you asked for, ask for another card: ")
                    PLAYER_HAND, PLAYER_SCORE = Make_Books(PLAYER_HAND,PLAYER_SCORE)
                    PLAYER_HAND.sort()
                    print ("YOUR HAND: ",PLAYER_HAND,"\n")
                    reponse = Computer_Response(COMPUTER_HAND, difficulty_level,card_2) # function to determine computer response
                    num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_2)
                    #if computer has what the player asked for
                    if response == True:
                        SUCCESS_COUNTER +=1
                        PLAYER_HAND = add_cards(PLAYER_HAND,card_2,num_cards)
                        COMPUTER_HAND = remove_cards(COMPUTER_HAND,card_2,num_cards)
                        PLAYER_HAND, PLAYER_SCORE = Make_Books(PLAYER_HAND,PLAYER_SCORE)
                        print ("YOUR HAND: ", PLAYER_HAND, "\n")
                    #if computer does not have what the player asked for
                    else:
                        if not Go_Fish():
                            drawn_card = deck[random.randint(0,len(deck)-1)]
                            PLAYER_HAND.append(drawn_card)
                            deck.remove(drawn_card)
                            PLAYER_HAND, PLAYER_SCORE = Make_Books(PLAYER_HAND,PLAYER_SCORE)
                            PLAYER_HAND.sort()
                            print ("YOUR HAND: ",PLAYER_HAND,"\n")
                else:
                    PLAYER_HAND.sort()
                    print ("YOUR HAND:",PLAYER_HAND,"\n")

    #check to see if player has books       
    PLAYER_HAND, PLAYER_SCORE = Make_Books(PLAYER_HAND,PLAYER_SCORE)
    if len(deck) != 0 or len(PLAYER_HAND) != 0 or len(COMPUTER_HAND) !=0: # while game is going
        Computer_Turn()
    else:
        End_Game()

#computer turn
def Computer_Turn():
    global PLAYER_SCORE
    global COMPUTER_SCORE
    global COMPUTER_HAND
    global PLAYER_HAND
    global TURN_COUNTER
    global GF_COUNTER
    global SUCCESS_COUNTER
    global deck
    global difficulty_level

    TURN_COUNTER +=1
    ## handles case when computer's hand is empty and there is still a deck. It draws a card and passes the turn. 
    if len(COMPUTER_HAND) == 0 and len(deck) != 0:
        drawn_card = deck[random.randint(0,len(deck)-1)]
        COMPUTER_HAND.append(drawn_card)
        deck.remove(drawn_card)
        Player_Turn()
    #if the computer's hand is not empty
    elif len(COMPUTER_HAND) != 0:
        #Easy difficulty
        if difficulty_level == "1":
            card_asked = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-1)]
            print ("Computer: Do you have any",card_asked,"\n")
            num_cards = num_cards_of_type_asked(PLAYER_HAND,card_asked)
            # if player has what computer asked for add cards to player hand and remove from computer hand
            if card_asked in PLAYER_HAND:
                SUCCESS_COUNTER += 1 
                COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
                COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
                print("The computer took your ",card_asked,"\n")
            else:
                if not Go_Fish():#checks to see if there are cards in the deck that can be drawn
                    drawn_card = deck[random.randint(0,len(deck)-1)]
                    COMPUTER_HAND.append(drawn_card)
                    deck.remove(drawn_card)
                    #if computer draws what it asks for it asks again
                    if drawn_card == card_asked:
                       print ("Computer: I got what I asked for!\n")
                       COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
                       card_asked2 = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-2)]
                       print ("Computer: Do you have any",card_asked2,"\n")
                       num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
                       # if player has what computer asked for add cards to player hand and remove from computer hand
                       if card_asked in PLAYER_HAND:
                           SUCCESS_COUNTER += 1
                           COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                           PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_Cards)
                           COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
                       else:
                           if not Go_Fish(): #checks to see if there are cards in the deck to draw
                               drawn_card_2 = deck[random.randint(0,len(deck)-1)]
                               COMPUTER_HAND.append(drawn_card_2)
                               deck.remove(drawn_card_2)
                               COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
            #check to see if game is over, if not go to the next player
            COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
            if len(deck) != 0 or len(PLAYER_HAND) != 0 or len(COMPUTER_HAND) !=0: # while game is going
                Player_Turn()
            else:
                End_Game()
                        
        # Medium and Hard Difficulty: NOTE: The computer uses the same strategy to pick which card to ask for.
        # The difference in difficulty is in the response to the users request.
        if difficulty_level == "2" or difficulty_level =="3":
            card_asked = COMPUTER_HAND[len(COMPUTER_HAND)-1]
            print ("Computer: Do you have any",card_asked, "\n")
            num_cards = num_cards_of_type_asked(PLAYER_HAND,card_asked)
            # if player has what computer asked for add cards to player hand and remove from computer hand
            if card_asked in PLAYER_HAND:
                SUCCESS_COUNTER +=1
                COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
                COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
                print("The computer took your ",card_asked,"\n")
            else:
                if not Go_Fish():#checks to make sure there are cards in the deck to draw
                    drawn_card = deck[random.randint(0,len(deck)-1)]
                    COMPUTER_HAND.append(drawn_card)
                    deck.remove(drawn_card)
                    #if computer draws the card it asked for it asks again
                    if drawn_card == card_asked:
                       print ("Computer: I got what I asked for!\n")
                       COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
                       card_asked2 = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-2)]
                       print ("Computer: Do you have any",card_asked2,"\n")
                       num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
                       # if player has what computer asked for add cards to player hand and remove from computer hand
                       if card_asked in PLAYER_HAND:
                           SUCCESS_COUNTER += 1
                           COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                           PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_Cards)
                           COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
                       else:
                           if not Go_Fish():#checks to make sure that there are cards in the deck to draw
                               drawn_card_2 = deck[random.randint(0,len(deck)-1)]
                               COMPUTER_HAND.append(drawn_card_2)
                               deck.remove(drawn_card_2)
            # checks to see if game is over, if not goes to next turn
            COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND, COMPUTER_SCORE)
            if len(deck) != 0 or len(PLAYER_HAND) != 0 or (COMPUTER_HAND !=0): # while game is going
                Player_Turn()
            else:
                End_Game()
                
    else:
        End_Game()


Player_Turn()
