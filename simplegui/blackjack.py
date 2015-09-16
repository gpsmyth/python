# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
dealer_hand = []
plyaer_hand = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    def __init__(self):
        # create Hand object
        self.value = 0
        self.hasAce = False
        self.cards = []
        
    def __str__(self):
        # return a string representation of a hand
        hand_str = "Hand Contains "
        
        for card in self.cards :
            hand_str += card.__str__() + " "
        
        return hand_str
    
    def add_card(self, card):
        # add a card object to a hand
        self.cards.append( card )

    def get_value(self):
        self.value = 0
        self.hasAce = False

        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        # return VALUES[ self.rank ]
        for card in self.cards :
            if card.rank == 'A' and self.hasAce == False : 
                # == is equaltity testing wheras 'is' is identity testing
                self.hasAce = True
                
            # Evaluate all cards, ACE defaults to 1    
            self.value += VALUES[card.rank]
            
        if self.hasAce == True and self.value + 10 <= 21:
            # Process for Ace card(s)
            self.value += 10
                        
        return self.value
        
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.cards :
            card.draw( canvas, pos )
            pos[0] += 90
            
                         
class Deck:
    def __init__(self):
        self.cards = []	# create a Deck object
        #for [ suit in SUITS for rank in RANKS self.cards.append( CARD ( suit, rank ())]
        # self.cards = [ [suit, rank]  for suit in SUITS for rank in RANKS ]
        self.cards = [ Card(suit, rank) for suit in SUITS for rank in RANKS ]
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle( self.cards )    # use random.shuffle()

    def deal_card(self):
        return self.cards.pop()	# deal a card object from the deck
    
    def __str__(self):	
        # return a string representing the deck
        deck_str = "Deck Contains "
        
        # print self.cards
        for card in self.cards :
            # deck_str += str( card[0] ) + str( card[1] ) + " "
            deck_str += card.__str__() + " "
            # deck_str += Card( suit, rank ).__str__() + " "
        
        return deck_str


#define event handlers for buttons
def deal():
    global outcome, in_play
    global player_hand, dealer_hand
    global deck
    
    if in_play == True :
        score -= 1
        outcome = "Player lost due to re-deal"
        in_play = False
        return
        
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    in_play = True
    deck.shuffle()
    outcome = ""
    
    for i in range ( 2 ) :
        player_hand.add_card( deck.deal_card() )
        dealer_hand.add_card( deck.deal_card() )
                
    print "Player: ", player_hand, "Dealer", dealer_hand
    print player_hand.get_value()
    print dealer_hand.get_value()

def hit():
    global outcome, in_play
    global player_hand, score
    global deck
 
    # if the hand is in play, hit the player
    if in_play == True :
        player_hand.add_card( deck.deal_card() )
        # if busted, assign a message to outcome, update in_play and score
        print "Player : ", player_hand
        print player_hand.get_value() 
        if player_hand.get_value() > 21 :
            outcome = "You went bust and lose"
            score -= 1
            in_play = False
        
        print "Outcome : ", outcome, "score : ", score

        
def stand():
    global outcome, in_play
    global dealer_hand, player_hand, score
    global deck
      
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True :
        while dealer_hand.get_value() < 17 :
            dealer_hand.add_card( deck.deal_card() )
        
        # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() > 21 :
            outcome = "Dealer went bust and you win"
            score += 1
        else :
            if player_hand.get_value() <= dealer_hand.get_value() :
                outcome = "Dealer wins"
                score -= 1
            else :
                outcome = "You win"
                score += 1
        
        in_play = False
                

# draw handler    
def draw(canvas):
    global outcome, in_play, score
    
    # test to make sure that card.draw works, replace with your code below
    # card = Card("S", "A")
    # card.draw(canvas, [300, 300])

    canvas.draw_text('Blackjack', (100, 100), 45, 'Gray', 'serif')
    canvas.draw_text('Score', (380, 100), 25, 'Black', 'serif')
    canvas.draw_text( str(score), (460, 100), 25, 'Black', 'serif')
    canvas.draw_text('Dealer', (100, 150), 25, 'Black', 'serif')
    canvas.draw_text('Player', (100, 350), 25, 'Black', 'serif')
    canvas.draw_text( outcome, (280, 150), 25, 'Black', 'serif')
    
    dealer_hand.draw( canvas, [100, 170] )
    player_hand.draw( canvas, [100, 380] )
    
    if in_play == True :
        canvas.draw_text( 'Hit or Stand?', (280, 350), 25, 'Black', 'serif')
        # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [136, 218], CARD_BACK_SIZE)
    else :
        canvas.draw_text( 'New Deal?', (280, 350), 25, 'Black', 'serif')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
