# implementation of card game - Memory

import simplegui
import random

WIDTH = 800
HEIGHT = 100
CARD_WIDTH = WIDTH // 16

DEDUG_LEVEL = 0 # Granular Debugging onto Console

card_list = [] # Empty list
card_len, mem_turns = 0, 0
exposed_list = []
# Selection list is used to capture the last 2 choices of
#    card_list index key and value
sel_vlist = []  # will only contain at most 2 elements (values)
sel_ilist = []  # (index tracking)
game_state = 0

# helper function to initialize globals
def new_game():
    global card_list, card_len, exposed_list, mem_turns
    global sel_ilist, sel_vlist, game_state
    
    game_state, mem_turns = 0, 0
    card_list = range( 8 ) + range( 8 ) 
    card_len = len( card_list)
    
    random.shuffle( card_list )
    exposed_list = [ False for i in range( card_len ) ]
    
    sel_ilist, sel_vlist = [], []

     
# define event handlers
def mouseclick(pos):
    global game_state, sel_vlist, sel_ilist, mem_turns
    exposed_len = len( sel_vlist )
    
    exposed_index = pos[0] / CARD_WIDTH
    
    if exposed_list[ exposed_index ] == True :
        return     # Don't need to process
    else :
        exposed_list[ exposed_index ] = True
    
    # Factoring out
    if game_state == 0 or game_state == 1 :
        sel_vlist.append( card_list[exposed_index] )
        sel_ilist.append( exposed_index )
    
    # State logic
    if game_state == 0 :
        game_state = 1       
    elif game_state == 1 :
        game_state = 2       
    else :
        game_state = 1
        if exposed_len == 2 :
            # Increment a turn
            mem_turns += 1
            
            # A match wasn't found in the 2-pair, no duplicates found
            if sel_vlist[0] != sel_vlist[1] :
                exposed_list[ sel_ilist[0] ] = False
                exposed_list[ sel_ilist[1] ] = False
                    
            sel_ilist, sel_vlist = [], []
            sel_vlist.append(card_list[exposed_index])
            sel_ilist.append(exposed_index)

    if DEDUG_LEVEL == 1 :
        # Card canvas goes from card0 is 0 to 50, card
        print "Exp list is ", exposed_list
        print "Game state ", game_state, "Sel list (V) (I)", \
            sel_vlist, sel_ilist, " turns : ", mem_turns
        print
    
"""                        
 cards are logically 50x100 pixels in size 
   canvas.draw_text(text, point, font_size, font_color)
   canvas.draw_text(text, point, font_size, font_color, font_face)
"""
def draw(canvas):
    global    card_list, card_len, exposed_list
    
    for i, cardno in enumerate( card_list ) :
        # Draw Vertical lines
        canvas.draw_line([ CARD_WIDTH * i, 0 ],[ CARD_WIDTH * i, HEIGHT ], 1, "White" )
        if exposed_list[i] == True:
            canvas.draw_text( str( cardno ), [15 + ( CARD_WIDTH * i ), 60], 50, 'White' )
    label.set_text( 'Turns = ' + str( mem_turns ))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.set_canvas_background("Green")

frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
