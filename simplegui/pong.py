# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global WIDTH, HEIGHT
    global RIGHT, LEFT
    
    ball_pos = [ WIDTH / 2, HEIGHT / 2]
    
    point_x = random.randrange( 120, 240 )
    point_y = random.randrange( 60, 180 )
    
    if  ( direction == RIGHT ) :
        ball_vel = [ point_x / 60, point_y / 60 ]
    else :
        ball_vel = [ -point_x / 60, -point_y / 60 ]
    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global LEFT
    
    # Initialise
    score1, score2 = 0, 0
    paddle1_vel, paddle2_vel = 0, 0
    paddle1_pos, paddle2_pos = HEIGHT / 2, HEIGHT / 2
    spawn_ball( LEFT )

def draw( canvas ):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle_vel
    global HEIGHT, WIDTH, PAD_WIDTH, BALL_RADIUS 
    global HALF_PAD_HEIGHT, HALF_PAD_WIDTH
    global LEFT, RIGHT
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    ##
    # update ball position
    ball_pos[0] += ball_vel[0] # Horizontal position
    ball_pos[1] += ball_vel[1] # Vertical position
    
    # draw ball
    canvas.draw_circle( ball_pos, 20, 1, "White", "White" )
    
    # update paddle's vertical position, keep paddle on the screen
    # HALF_PAD_HEIGHT is referenced here so as ot determine the center of the paddle
    if ( paddle1_pos >= HALF_PAD_HEIGHT and paddle1_pos <= ( HEIGHT - HALF_PAD_HEIGHT )):
        paddle1_pos += paddle1_vel
    elif ( paddle1_pos <= HALF_PAD_HEIGHT ) :
        paddle1_pos = HALF_PAD_HEIGHT
    elif ( paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT ) :
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    
    # Paddle vel only increeased between restricted height limits from
    # HALF_PAD_HEIGHT to ( HEIGHT - HALF_PAD_HEIGHT )
    if paddle2_pos >= HALF_PAD_HEIGHT and paddle2_pos <= ( HEIGHT - HALF_PAD_HEIGHT ) :
        paddle2_pos += paddle2_vel
    elif paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT    
    
    # draw paddles
    canvas.draw_line( [ HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT ], \
                      [ HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT ], \
                      PAD_WIDTH, "White" )
    canvas.draw_line( [ WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT ], \
                      [ WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT ], \
                      PAD_WIDTH, "White" )

    
    # determine whether paddle and ball collide
    # Refelct the ball off the vertical walls, no need to consider refelction off
    # horizontal walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= ( HEIGHT - BALL_RADIUS ) :
        ball_vel[1] = -ball_vel[1]
    
    # LH Paddle affected  - check horizontal posn first
    if ( ball_pos[0] - BALL_RADIUS <= PAD_WIDTH ) :
        # Actual collission occurring - checking with vertical position
        if ( ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and  \
                          ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT ) :
            # Increase velocity by 10% and provide reflection             
            ball_vel[0] = -( ball_vel[0] * 1.1 )
            
    # RH Paddle affected  - check horizontal posn first      
    if ( ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH ) :
        # Actual collission occurring - checking with vertical position
        if ( ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT and \
                          ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT ) :
            # Increase velocity by 10% and provide reflection             
            ball_vel[0] = -( ball_vel[0] * 1.1 )
    
    # Deciding on new game
    if ( ball_pos[0] < PAD_WIDTH ) : # LH Paddle distance
        score2 += 1
        spawn_ball( RIGHT )
    elif ( ball_pos[0] > WIDTH - PAD_WIDTH ) : # RH Paddle distance
        spawn_ball( LEFT )
        score1 += 1
    
    # draw scores
    canvas.draw_text( str( score1 ) + "   " + str( score2 ), \
                     [ (WIDTH / 2) - 25, 30], 30, "White")
    

def keydown(key):
    global paddle1_vel, paddle2_vel
    
    # w and s are up / down keys for LHS player
    # up and down arrows are keys for RHS player
    if key == simplegui.KEY_MAP[ "w" ]:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP[ "s" ]:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP[ "up" ]:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP[ "down" ]:
        paddle2_vel = 4
   

def keyup(key):
    global paddle1_vel, paddle2_vel

    # w and s are up / down keys for LHS player
    # up and down arrows are keys for RHS player
    if key == simplegui.KEY_MAP[ "w" ]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP[ "s" ]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP[ "up" ]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP[ "down" ]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button( "Restart", new_game, 100 )


# start frame
new_game()
frame.start()
