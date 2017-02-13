import random
#NOTES: WHAT IF PLAYER HAND IS EMPTY AT ANY POINT
difficulty_level = input ("Welcome to Go Fish: the computer program! you can play go fish against a computer program here based on 3 different difficulty levels:\n"+
                          "1: The computer plays randomly.\n"+"2: The computer plays with some strategy.\n"+"3: The computer lies.\n")
deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]
PLAYER_HAND = []
COMPUTER_HAND = []
PLAYER_SCORE = 0
COMPUTER_SCORE = 0
LIES = 1
TOTAL_CARDS_PASSED = 0 # for stats
x=0
turn = 1

def Computer_Response(hand, level, card):
    global LIES
##    print (hand, level, card)
    response = False
    ## on computer's turn
    if level == "1":
##        print (hand, level, card)
        if card in hand:
            response = True
        return response
        #computer chooses card to ask for at random from cards in its hand
##        ask_for = random.randint(0,len(COMPUTER_HAND)-1)
        
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
    


#function to determine books
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
    num_cards = 0
    for x in hand:
        if x==card:
            num_cards+=1
    TOTAL_CARDS_PASSED += num_cards

    return num_cards

def Go_Fish(turn):
    global deck
    if deck == [] or deck == 0 or deck == None:
        if turn is 1:
            Player_Turn()
        else:
            Computer_Turn()

    else:
        print ("\nGo fish...\n")

def make_books(player, counter):
    # index of rank array is a mapping to num_decks
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # counters of number of cards of a given rank in the hand
    num_decks = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in player:
        # increments appropriate rank counter for each card
        num_decks[ranks.index(card)] +=1
    for i in range(12):
        # 4 cards of a rank in the hand
        if num_decks[i]>= 4:
            # increment deck counter
            counter+=1
            # remove deck from hand
            player = [x for x in player if not ranks[i] in x]
    return player, counter

#deal initial hand?

while x<7:
    
    player_card = random.randint(0,len(deck)-1)
    #print (player_card)
    #print (deck[player_card])
    PLAYER_HAND.append(deck[player_card])
    del deck[player_card]
    computer_card = random.randint(0,len(deck)-1)
    #print (computer_card)
    #print (deck[computer_card])
    COMPUTER_HAND.append(deck[computer_card])
    del deck[computer_card] 
    x+=1

    

##while len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
#print ("YOUR HAND: ",(PLAYER_HAND))


def Player_Turn():
    global PLAYER_SCORE
    global COMPUTER_SCORE
    print ("Score: \t Player: ",PLAYER_SCORE,"Computer: ",COMPUTER_SCORE)
    global COMPUTER_HAND
    global PLAYER_HAND
    
    global deck
    if PLAYER_HAND == 0 or PLAYER_HAND == None or PLAYER_HAND == []:
        drawn_card = deck[random.randint(0,len(deck)-1)]
        PLAYER_HAND.append(drawn_card)
        deck.remove(drawn_card)
    else:
        print("YOUR HAND: ",PLAYER_HAND,"\n")
        card = input ("What do you ask for? ")
        response = Computer_Response(COMPUTER_HAND, difficulty_level, card) # function to determine computer response
        if response == True:
            print("You got what you asked for!\n")
            num_cards = num_cards_of_type_asked(COMPUTER_HAND,card)
            PLAYER_HAND = add_cards(PLAYER_HAND,card,num_cards)
            COMPUTER_HAND = remove_cards(COMPUTER_HAND,card,num_cards)
            PLAYER_HAND.sort()
            print ("YOUR HAND: ",PLAYER_HAND,"\n")
            print (COMPUTER_HAND) ##delete P
        else:
            Go_Fish(0)
            drawn_card = deck[random.randint(0,len(deck)-1)]
            PLAYER_HAND.append(drawn_card)
            deck.remove(drawn_card)
            print("You drew a ",drawn_card,"\n")
            if drawn_card == card:
                print ("YOUR HAND: ",PLAYER_HAND,"\n")
                card_2 = input ("You drew what you asked for, ask for another card: \n")
                PLAYER_HAND.sort()
                reponse = Computer_Response(COMPUTER_HAND, difficulty_level,card_2) # function to determine computer response
                num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_2)
                if response == True:
                    PLAYER_HAND = add_cards(PLAYER_HAND,card_2,num_cards)
                    COMPUTER_HAND = remove_cards(COMPUTER_HAND,card_2,num_cards)

                else:
                    Go_Fish(0)
                    #print("\nComputer: Go fish!\n")
                    drawn_card = deck[random.randint(0,len(deck)-1)]
                    PLAYER_HAND.append(drawn_card)
                    deck.remove(drawn_card)
                    PLAYER_HAND.sort()
                    print ("YOUR HAND: ",PLAYER_HAND,"\n")
            else:
                #drawn_card = deck[random.randint(0,len(deck)-1)]
                ##PLAYER_HAND.append(drawn_card)
                
                PLAYER_HAND.sort()
                print ("YOUR HAND:",PLAYER_HAND,"\n")
    PLAYER_HAND, PLAYER_SCORE = make_books(PLAYER_HAND,PLAYER_SCORE)
    if len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
        #print("YOUR HAND: ",PLAYER_HAND,"\n")
        Computer_Turn()
    else:
        print("End game")

def Computer_Turn():
    global COMPUTER_HAND
    global COMPUTER_SCORE
    global PLAYER_HAND
    global PLAYER_SCORE
    global deck
    global difficulty_level
    if COMPUTER_HAND == 0 or COMPUTER_HAND == None or COMPUTER_HAND == []:
        drawn_card = deck[random.randint(0,len(deck)-1)]
        PLAYER_HAND.append(drawn_card)
        deck.remove(drawn_card)
    else:
        if difficulty_level == "1":
            card_asked = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-1)]
            print ("Computer: Do you have any",card_asked,"\n")
            num_cards = num_cards_of_type_asked(PLAYER_HAND,card_asked)
            if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
                COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
                print("The computer took your ",card_asked,"\n")
            else:
                Go_Fish(1)
                drawn_card = deck[random.randint(0,len(deck)-1)]
                COMPUTER_HAND.append(drawn_card)
                deck.remove(drawn_card)
                print(COMPUTER_HAND) 
                if drawn_card == card_asked: ##ERROR IF DRAWN CARD = CARD ASKED
                   print ("I got what I asked for!\n")
                   card_asked2 = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-2)]
                   print ("Do you have any",card_asked2,"\n")
                   num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
                   if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
                       COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                       PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_Cards)
                   else:
                       Go_Fish(1)
                       drawn_card_2 = deck[random.randint(0,len(deck)-1)]
                       COMPUTER_HAND.append(drawn_card_2)
                       deck.remove(drawn_card)
            COMPUTER_HAND, COMPUTER_SCORE = make_books(COMPUTER_HAND,COMPUTER_SCORE)
            if len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
                Player_Turn()
                        
        # Medium Difficulty 
        if difficulty_level == "2":
            card_asked = COMPUTER_HAND[len(COMPUTER_HAND)-1]
            print ("Do you have any",card_asked, "\n")
            num_cards = num_cards_of_type_asked(PLAYER_HAND,card_asked)
            if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
                COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
                print("The computer took your ",card_asked,"\n")
    ##            print ("comp hand", COMPUTER_HAND)
            else:
                Go_Fish(1)
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
                       COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                       PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_Cards)
                   else:
                       Go_Fish(1)
                       drawn_card_2 = deck[random.randint(0,len(deck)-1)]
                       COMPUTER_HAND.append(drawn_card_2)
                       deck.remove(drawn_card)
            COMPUTER_HAND, COMPUTER_SCORE = make_books(COMPUTER_HAND,COMPUTER_SCORE)
            if len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
                Player_Turn()
                
        #Hard Difficulty    
        if difficulty_level == "3":
            card_asked = COMPUTER_HAND[len(COMPUTER_HAND)-1]
            print ("Do you have any",card_asked, "\n")
            num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
            if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
                COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
                print("The computer took your ",card_asked,"\n")
            else:
                Go_Fish(1)
                drawn_card = deck[random.randint(0,len(deck)-1)]
                COMPUTER_HAND.append(drawn_card)
                print ("comp hand", COMPUTER_HAND)
                deck.remove(drawn_card)
                if drawn_card == card_asked:
                   print ("Computer got what it asked for!\n")
                   card_asked2 = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-2)]
                   print ("Do you have any",card_asked2,"\n")
                   num_cards = num_cards_of_type_asked(COMPUTER_HAND,card_asked)
                   if card_asked in PLAYER_HAND: #NEEDS TO CHECK THE NUMBER OF COPYIES OF THE CARD IN OTHER HAND
                       COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                       PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_Cards)
                   else:
                       Go_Fish(1)
                       drawn_card_2 = deck[random.randint(0,len(deck)-1)]
                       COMPUTER_HAND.append(drawn_card_2)
                       deck.remove(drawn_card)
            COMPUTER_HAND, COMPUTER_SCORE = make_books(COMPUTER_HAND,COMPUTER_SCORE)
            if len(deck) != 0 and PLAYER_HAND != 0 and COMPUTER_HAND !=0: # while game is going
                Player_Turn()


Player_Turn()
