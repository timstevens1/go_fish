import random
from deck import Deck
import time

# initialize global variables for player hands, score and end game statistics.
# AUTHORS: EMMA TAIT and TIM STEVENS
PLAYER_HAND = []
COMPUTER_HAND = []
PLAYER_SCORE = 0
COMPUTER_SCORE = 0
LIES = 1
TOTAL_CARDS_PASSED = 0 # for stats
GF_COUNTER = 0
SUCCESS_COUNTER = 0
START_TIME = 0
END_TIME = 0
TURN_COUNTER = 0
CARD_FREQUENCY = [0,0,0,0,0,0,0,0,0,0,0,0,0]
RANK = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = Deck()
PLAYER_HAND, COMPUTER_HAND, deck = deck.deal_hands()
LAST_ASKED = ''
ASK_INDEX = 0



#input validation for difficulty level
###AUTHOR: JOSE VILA
difficulty_level = None
while difficulty_level is None:
    difficulty_level_value = input(
        "Welcome to Go Fish: the computer program!\n\nGo fish is a game where you try to get as many sets of four of a\nkind (called books) as possible. To do this, you may ask the computer for\n"
        +"a card each turn. You must have the card in your hand in order to be able to ask for it. \n\nIf the computer has the card you requested it will give it to you. If not it will tell you\n"
        +"to 'Go Fish' and you will draw a card. Then it will be the computer's turn. The computer will \ngo through the same process. If you have the card that the computer asked for it will\n"
        +"take the card, if not it will draw. \n\nWhen you have four cards of the same rank they will be removed from your \nhand and you will score one point. The game ends when ther are no more\n"
        +"cards in the deck or in either player's hand (they have all been played as books).\n\nYou can play go fish against a computer program here based on 3 different difficulty levels:\n" +
        "1: The computer plays randomly.\n" + "2: The computer plays with some strategy.\n" + "3: The computer lies.\n")
    #make sure only integers are entered
    try:
        difficulty_level = int(difficulty_level_value)
    except ValueError:
        print("I'm sorry. {input} is not a number.".format(input=difficulty_level_value))
        difficulty_level = None
        continue
    else:
        
        #successful input!
        #now validate the number
        if difficulty_level > 3 or difficulty_level == 0:
            print("The number you input is not a difficulty level")
            difficulty_level = None
            continue
        #successful difficulty level entered! break the loop
        else:
            START_TIME = time.time()
            break

## This method determines the computer's response to players requests
## depending on the difficulty level
###AUTHOR: EMMA TAIT
def Computer_Response(hand, level, card):
    global LIES
    response = False
    if level == 1:
        if card in hand:
            response = True
        return response
        #computer chooses card to ask for at random from cards in its hand
        
    if level == 2:
        if card in hand:
            response = True
        return response
        #computer asks for card drawn or rotates through other cards

    if level == 3:
        if card in hand and LIES != 3:
            response = True
            LIES += 1
        if card in hand and LIES == 3:
            response = False
            LIES = 1
        return response
          
        #computer lies every 3rd time it has what player asks for
    



# adds correct number of cards to hand that asked for them
###AUTHORS EMMA TAIT
def add_cards(hand,card,num):
    x = 0
    while x < num:
        hand.append(card)
        x += 1
    return hand
    
#removes the correct number of cards from the hand that had them
###AUTHORS: EMMA TAIT
def remove_cards(hand,card,num):
    x = 0
    while x < num:
        hand.remove(card)
        x += 1
    return hand

#gets the number of cards of the type asked for from the asked hand
#also collects statistic information on cards
###AUTHORS: EMMA TAIT AND TIM STEVENS
def num_cards_of_type_asked(hand,card):
    global TOTAL_CARDS_PASSED
    global RANK
    global CARD_FREQUENCY
    num_cards = 0
    for x in hand:
        if x==card:
            num_cards+=1
    TOTAL_CARDS_PASSED += num_cards
    CARD_FREQUENCY[RANK.index(card)] += 1
    return num_cards

#makes sure that the deck is not empty before they draw a card.
###AUTHOR: EMMA TAIT
def Go_Fish():
    global deck
    global GF_COUNTER
    deck_empty = False
    if len(deck) == 0:
        deck_empty = True
    else:
        time.sleep(0.5)
        print ("\nGo fish...\n")
        time.sleep(0.5)
        GF_COUNTER +=1
    return deck_empty


#determine if player has books of cards and tally score.
### AUTHOR: TIM STEVENS
def Make_Books(player, counter):
    # index of rank array is a mapping to num_decks
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # counters of number of cards of a given rank in the hand
    num_card_type = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in player:
        # increments appropriate rank counter for each card
        num_card_type[ranks.index(card)] +=1
    for i in range(13):
        # 4 cards of a rank in the hand
        if num_card_type[i]>= 4:
            # increment deck counter
            counter+=1
            # remove deck from hand
            player = [x for x in player if not ranks[i] in x]
    return player, counter


#print statistics at the end of the game.
###AUTHOR: TIM STEVENS
def End_Game():
    global TOTAL_CARDS_PASSED
    global PLAYER_SCORE
    global COMPUTER_SCORE
    global GF_COUNTER
    global START_TIME
    global SUCCESS_COUNTER
    global TURN_COUNTER
    global CARD_FREQUENCY
    global RANK
    global END_TIME
    END_TIME = time.time()

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
        print('Game duration: {0:.2f}'.format((END_TIME-START_TIME)/60),"minutes")


    
#the players turn. Allows the player to request a card. Gets the card if the computer has it, if not draws a card.
# if the card the player draws is the card they asked for they get to go again.
#AUTHOR: EMMA TAIT and KYLE WHALEN (debugging)
def Player_Turn():
    global PLAYER_SCORE
    global GF_COUNTER
    global SUCCESS_COUNTER
    global COMPUTER_SCORE
    global COMPUTER_HAND
    global PLAYER_HAND
    global deck
    print ("Score: \t Player: ",PLAYER_SCORE,"Computer: ",COMPUTER_SCORE)
    #Handles case if player's hand is empty and the deck is not
    if len(PLAYER_HAND) == 0  and len(deck) !=0 :
        drawn_card = deck[random.randint(0,len(deck)-1)]
        PLAYER_HAND.append(drawn_card)
        deck.remove(drawn_card)
        Computer_Turn()
    #if players hand is not empty.
    elif len(PLAYER_HAND) !=0:
        PLAYER_HAND.sort()
        print("YOUR HAND: ",PLAYER_HAND,"\n")
        time.sleep(0.7)
        #validates card input from user
        ###AUTHOR: JOSE VILA
        card = None
        while card is None:
            card = input("What do you ask for? ").upper() #allows user to enter lowercase letters for Jack Queen King and Ace ranks
            time.sleep(0.5)
            if card not in PLAYER_HAND:
                print("The card you asked for is not in your hand. Try again. ")
                card = None
                continue
            else:
                break
        ###AUTHOR: EMMA TAIT
        response = Computer_Response(COMPUTER_HAND, difficulty_level, card)
        #if computer has what the player asked for pass the cards
        if response == True:
            SUCCESS_COUNTER +=1
            print("You got what you asked for!\n")
            time.sleep(0.7)
            num_cards = num_cards_of_type_asked(COMPUTER_HAND,card)
            PLAYER_HAND = add_cards(PLAYER_HAND,card,num_cards)
            COMPUTER_HAND = remove_cards(COMPUTER_HAND,card,num_cards)
            #check for books
            PLAYER_HAND, PLAYER_SCORE = Make_Books(PLAYER_HAND,PLAYER_SCORE)
            PLAYER_HAND.sort()
            print ("YOUR HAND: ",PLAYER_HAND,"\n")
            time.sleep(0.7)
        #if computer does not have what the player asked for
        else:
            if not Go_Fish():#checks if there are cards in the deck to draw
                drawn_card = deck[random.randint(0,len(deck)-1)]
                PLAYER_HAND.append(drawn_card)
                deck.remove(drawn_card)
                print("You drew a ",drawn_card,"\n")
                time.sleep(0.7)   
                PLAYER_HAND.sort()
                print ("YOUR HAND:",PLAYER_HAND,"\n")
                time.sleep(0.7)

    #check to see if player has books       
    PLAYER_HAND, PLAYER_SCORE = Make_Books(PLAYER_HAND,PLAYER_SCORE)
    #checks to make sure game is running, if so, passes the turn to the computer
    if len(deck) != 0 or len(PLAYER_HAND) != 0 or len(COMPUTER_HAND) !=0: # while game is going
        Computer_Turn()
    else:
        End_Game()

#computer turn. Allows the computer to request a card. Gets the card if the player has it, if not draws a card.
# if the card the player draws is the card they asked for they get to go again.
#AUTHOR: EMMA TAIT and KYLE WHALEN (debugging)
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
        if difficulty_level == 1:
            card_asked = COMPUTER_HAND[random.randint(0,len(COMPUTER_HAND)-1)]
            print ("Computer: Do you have any",card_asked,"\n")
            time.sleep(0.7)
            num_cards = num_cards_of_type_asked(PLAYER_HAND,card_asked)
            # if player has what computer asked for add cards to player hand and remove from computer hand
            if card_asked in PLAYER_HAND:
                SUCCESS_COUNTER += 1 
                COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
                #check for books
                COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
                print("The computer took your ",card_asked,"\n")
                time.sleep(0.7)
            else:
                if not Go_Fish():#checks to see if there are cards in the deck that can be drawn
                    drawn_card = deck[random.randint(0,len(deck)-1)]
                    COMPUTER_HAND.append(drawn_card)
                    deck.remove(drawn_card)
            #check to see if game is over, if not go to the next player
            COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
            if len(deck) != 0 or len(PLAYER_HAND) != 0 or len(COMPUTER_HAND) !=0: # while game is going
                Player_Turn()
            else:
                End_Game()
                        
        # Medium and Hard Difficulty: NOTE: The computer uses the same strategy to pick which card to ask for.
        # The difference in difficulty is in the response to the users request.
        ###AUTHOR: EMMA TAIT and KYLE WHALEN (debugging)
        if difficulty_level == 2 or difficulty_level == 3:
            #makes sure that computer asks for most recent card drawn unless that was what it asked for the
            #previous turn in which case it iterates through its hand. 
            global LAST_ASKED
            global ASK_INDEX
            if LAST_ASKED != '':
                ASK_INDEX = COMPUTER_HAND.index(LAST_ASKED)
            print ("comp hand",COMPUTER_HAND)
            card_asked = COMPUTER_HAND[len(COMPUTER_HAND)-1]
            COMPUTER_HAND.sort()
            print ("comp hand",COMPUTER_HAND)
            if card_asked == LAST_ASKED:
                for card in COMPUTER_HAND:
                    if card == card_asked:
                        ASK_INDEX += 1
                        print(ASK_INDEX)
                if ASK_INDEX < len(COMPUTER_HAND):
                    card_asked = COMPUTER_HAND[ASK_INDEX]
                    ASK_INDEX += 1
                    
                else:
                    ASK_INDEX = 0
                    card_asked = COMPUTER_HAND[ASK_INDEX]
            LAST_ASKED = card_asked
            print ("Computer: Do you have any",card_asked, "\n")
            time.sleep(0.7)
            num_cards = num_cards_of_type_asked(PLAYER_HAND,card_asked)
            # if player has what computer asked for add cards to player hand and remove from computer hand
            if card_asked in PLAYER_HAND:
                SUCCESS_COUNTER +=1
                COMPUTER_HAND = add_cards(COMPUTER_HAND,card_asked,num_cards)
                PLAYER_HAND = remove_cards(PLAYER_HAND,card_asked,num_cards)
                #check for books
                COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND,COMPUTER_SCORE)
                print("The computer took your ",card_asked,"\n")
                time.sleep(0.7)
            else:
                if not Go_Fish():#checks to make sure there are cards in the deck to draw
                    drawn_card = deck[random.randint(0,len(deck)-1)]
                    COMPUTER_HAND.append(drawn_card)
                    deck.remove(drawn_card)

            # checks to see if game is over, if not goes to next turn
            COMPUTER_HAND, COMPUTER_SCORE = Make_Books(COMPUTER_HAND, COMPUTER_SCORE)
            if len(deck) != 0 or len(PLAYER_HAND) != 0 or (COMPUTER_HAND !=0): # while game is going
                Player_Turn()
            else:
                End_Game()
                
    else:
        End_Game()

#initializes first turn
Player_Turn()
