import random
import time
#NOTES: WHAT IF PLAYER HAND IS EMPTY AT ANY POINT
difficulty_level = input ("1 = easy\n2 = medium\n3 = hard\n")
deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]
print (difficulty_level)
PLAYER_HAND = []
COMPUTER_HAND = []
PLAYER_SCORE = 0
COMPUTER_SCORE = 0
LIES = 1
# for stats
TOTAL_CARDS_PASSED = 0
GF_COUNTER = 0
SUCCESS_COUNTER = 0
TIME_COUNTER = 0
TURN_COUNTER = 0
CARD_FREQUENCY = [0,0,0,0,0,0,0,0,0,0,0,0,0]
RANK = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

x=0
turn = 1


def Computer_Response(hand, level, card):
    global LIES
#    print (hand, level, card)
    response = False
    # on computer's turn
    if level == "1":
#   print (hand, level, card)
        if card in hand:
            response = True
        return response
#       computer chooses card to ask for at random from cards in its hand
#        ask_for = random.randint(0,len(COMPUTER_HAND)-1)
        
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
    

##function to determine books
##def books(hand)

def add_cards(hand,card,num):
    x = 0
    while x < num:
        hand.append(card)
        x += 1
    return hand
    

def remove_cards(hand,card,num):
    x = 0
    while x < num:
        hand.remove(card)
        x += 1
    return hand


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


def end_game():
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

    if COMPUTER_SCORE > PLAYER_SCORE:
        print('Congratulations! You lost!')
        print('Game Stats:\n')
        print('Your Score: {}'.format(PLAYER_SCORE))
        print('Computer Score: {}'.format(COMPUTER_SCORE))
        print('Total cards passed: {}'.format(TOTAL_CARDS_PASSED))
        print('Total times players went fish: {}'.format(GF_COUNTER))
        print('Total correct guesses: {}'.format(SUCCESS_COUNTER))
        print('Most common card: {} occurred {} times'.format(most_common_card,max(CARD_FREQUENCY)))
        print('Least common card: {} occurred {} times'.format(least_common_card,min(CARD_FREQUENCY)))
        print('Mean number of cards passed per turn: {}'.format(avg_card_passed))
        print('Number of turns: {}'.format(TURN_COUNTER))
        print('Game duration: {}'.format(TIME_COUNTER))
    else:
        print('Congratulations! You won!')
        print('Game Stats:\n')
        print('Your Score: {}'.format(PLAYER_SCORE))
        print('Computer Score: {}'.format(COMPUTER_SCORE))
        print('Total cards passed: {}'.format(TOTAL_CARDS_PASSED))
        print('Total times players went fish: {}'.format(GF_COUNTER))
        print('Total correct guesses: {}'.format(SUCCESS_COUNTER))
        print('Most common card: {} occurred {} times'.format(most_common_card, max(CARD_FREQUENCY)))
        print('Least common card: {} occurred {} times'.format(least_common_card, min(CARD_FREQUENCY)))
        print('Mean number of cards passed per turn: {}'.format(avg_card_passed))
        print('Number of turns: {}'.format(TURN_COUNTER))
        print('Game duration: {}'.format(TIME_COUNTER))


while x < 7:
    player_card = random.randint(0,len(deck)-1)
    print (player_card)
    print (deck[player_card])
    PLAYER_HAND.append(deck[player_card])
    del deck[player_card]
    computer_card = random.randint(0,len(deck)-1)
    print (computer_card)
    print (deck[computer_card])
    COMPUTER_HAND.append(deck[computer_card])
    del deck[computer_card] 
    x+=1


##while len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
print ("YOUR HAND: ",(PLAYER_HAND))
print ("Player: ",PLAYER_SCORE,"Computer: ",COMPUTER_SCORE)


def Player_Turn():
    global TIME_COUNTER
    global COMPUTER_HAND
    global PLAYER_HAND
    global GF_COUNTER
    global SUCCESS_COUNTER
    global deck
    TIME_COUNTER = time.time()
    card = input ("What do you ask for? ")
    response = Computer_Response(COMPUTER_HAND, difficulty_level, card) # function to determine computer response
    if response:
        SUCCESS_COUNTER +=1
        num_cards = num_cards_of_type_asked(COMPUTER_HAND,card)
        PLAYER_HAND = add_cards(PLAYER_HAND,card,num_cards)
        COMPUTER_HAND = remove_cards(COMPUTER_HAND,card,num_cards)
        PLAYER_HAND.sort()
        print ("YOUR HAND: ",PLAYER_HAND,"\n")
        print (COMPUTER_HAND)
    else:
        GF_COUNTER +=1
        drawn_card = deck[random.randint(0,len(deck)-1)]
        PLAYER_HAND.append(drawn_card)
        if drawn_card == card:
            card_2 = input ("You drew what you asked for, ask for another card: \n")
            PLAYER_HAND.sort()
            print ("YOUR HAND: ",PLAYER_HAND,"\n")
            reponse = Computer_Response(COMPUTER_HAND, difficulty_level,card_2) # function to determine computer response
            num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_2)
            if response == True:
                SUCCESS_COUNTER +=1
                PLAYER_HAND = add_cards(PLAYER_HAND,card_2,num_cards)
                COMPUTER_HAND = remove_cards(COMPUTER_HAND,card_2,num_cards)

            else:
                drawn_card = deck[random.randint(0,len(deck)-1)]
                PLAYER_HAND.append(drawn_card)
                deck.remove(drawn_card)
                PLAYER_HAND.sort()
                print ("YOUR HAND: ",PLAYER_HAND,"\n")
        else:
            drawn_card = deck[random.randint(0,len(deck)-1)]
            PLAYER_HAND.append(drawn_card)
            deck.remove(drawn_card)
            PLAYER_HAND.sort()
            print ("YOUR HAND:",PLAYER_HAND,"\n")
    if len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
        Computer_Turn()
    else:
        end_game()


def Computer_Turn():
    global COMPUTER_HAND
    global PLAYER_HAND
    global deck
    global TURN_COUNTER
    global GF_COUNTER
    global SUCCESS_COUNTER
    global difficulty_level
    TURN_COUNTER +=1
    if difficulty_level == "1":
        card_asked = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-1)]
        print ("Do you have any",card_asked,"\n")
        num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
        if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
            SUCCESS_COUNTER +=1
            COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
            PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
        else:
            GF_COUNTER +=1
            print ("Go Fish!\n")
            drawn_card = deck[random.randint(0,len(deck)-1)]
            COMPUTER_HAND.append(drawn_card)
            deck.remove(drawn_card)
            if drawn_card == card_asked:
               print ("I got what I asked for!\n")
               card_asked2 = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-2)]
               print ("Do you have any",card_asked2,"\n")
               num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
               if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
                   SUCCESS_COUNTER +=1
                   COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                   PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
               else:
                   print ("Go Fish\n")
                   drawn_card_2 = deck[random.randint(0,len(deck)-1)]
                   COMPUTER_HAND.append(drawn_card_2)
                   deck.remove(drawn_card)
        if len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
            Player_Turn()
        else:
            end_game()
                    
    # Medium Difficulty 
    if difficulty_level == "2":
        card_asked = COMPUTER_HAND[len(COMPUTER_HAND)-1]
        print ("Do you have any",card_asked, "\n")
        num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
        if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
            SUCCESS_COUNTER +=1
            COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
            PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
##            print ("comp hand", COMPUTER_HAND)
        else:
            GF_COUNTER +=1
            print ("Go Fish!\n")
            drawn_card = deck[random.randint(0,len(deck)-1)]
            COMPUTER_HAND.append(drawn_card)
##            print ("comp hand", COMPUTER_HAND)
            deck.remove(drawn_card)
            if drawn_card == card_asked:
               print ("I got what I asked for!\n")
               card_asked2 = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-2)]
               print ("Do you have any",card_asked2,"\n")
               num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
               if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
                   SUCCESS_COUNTER +=1
                   COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                   PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
               else:
                   print ("Go Fish\n")
                   drawn_card_2 = deck[random.randint(0,len(deck)-1)]
                   COMPUTER_HAND.append(drawn_card_2)
                   deck.remove(drawn_card)
        if len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
            Player_Turn()
        else:
            end_game()
    #Hard Difficulty    
    if difficulty_level == "3":
        card_asked = COMPUTER_HAND[len(COMPUTER_HAND)-1]
        print ("Do you have any",card_asked, "\n")
        num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
        if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
            SUCCESS_COUNTER +=1
            COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
            PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
        else:
            GF_COUNTER +=1
            print ("Go Fish!\n")
            drawn_card = deck[random.randint(0,len(deck)-1)]
            COMPUTER_HAND.append(drawn_card)
            print ("comp hand", COMPUTER_HAND)
            deck.remove(drawn_card)
            if drawn_card == card_asked:
               print ("I got what I asked for!\n")
               card_asked2 = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-2)]
               print ("Do you have any",card_asked2,"\n")
               num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
               if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
                   SUCCESS_COUNTER +=1
                   COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                   PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
               else:
                   print ("Go Fish\n")
                   drawn_card_2 = deck[random.randint(0,len(deck)-1)]
                   COMPUTER_HAND.append(drawn_card_2)
                   deck.remove(drawn_card)
        if len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
            Player_Turn()
        else:
            end_game()


Player_Turn()


