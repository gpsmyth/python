"""
Stopwatch program
This program is a stopwatch timer which tests
your reflexes to get a tenth of a second arriving
at a zero value
"""
import simplegui
import random

# Step 1 - Initialise Global Variables
"""
Step to consider for simplegui stopwatch implemtation
1 - Initialize global variables
2 - Define helper functions
3 - Define classes
4 - Define event handlers
5 - Create frame
6 - Register event handlers
7 - Start frame and timers
"""
# Initialise global variables
canvas_width, canvas_height = 220, 200
stopwatch_time, stopped_time = 0, 0 # stopped_time is the reflex part
started = False # Used to see if the stopwatch should be started
stop_count, matched_count = 0, 0  # matched_count is the reflex counter

# Step 2 - define helper functions
def format( time_val ) :
    """
    Helper function to convert int to str type of Mins:Secs:TenthsofSecs format
    Set the time string to Minutes:Seconds:Tenths from TenthsofSecs integer
    """
    return ( '%01d:%02d.%01d' % ( time_val / 600, \
                                 (time_val / 10) % 60, \
                                 time_val % 10 ))
    

# Step 3 - Define classes increment, start_button, stop_button, draw and restart
def increment():
    global stopwatch_time
    stopwatch_time += 1

    
def start_button() :
    global started
    
    started = True
    stopwatch_timer.start()

    
def stop_button():
    global stop_count
    global started
    global matched_count
    global stopped_time
    
    if started:
        stopwatch_timer.stop()
        started = False
        stop_count += 1
        if ( stopped_time % 10 == 0 ) :
            matched_count += 1
        
        
def draw(canvas):
    global stopped_time
    
    stopped_time = stopwatch_time
    
    #canvas.draw_text( str(stopwatch_time), [100, 100], 36, "White") 
    canvas.draw_text( format(stopwatch_time), [50, 100], 36, "White")
    canvas.draw_text( str(matched_count) + " / " + str(stop_count), \
                     [140, 30], 30, "Green")
        
def restart():
    global started, stopwatch_time, stop_count, matched_count
    
    started = False
    stopwatch_time, matched_count, stop_count, stopped_time = 0, 0, 0, 0
    
    stopwatch_timer.stop()

    
# Step 5 - Creating a frame
frame = simplegui.create_frame( "Stopwatch", canvas_width, canvas_height ) 

# Step 6 - Register event handlers
frame.set_draw_handler(draw)
stopwatch_timer = simplegui.create_timer(100, increment)
frame.add_button("Start", start_button, 100)
frame.add_button("Stop", stop_button, 100)
frame.add_button("Restart", restart, 100)

# Step 7 - Start Frame and stopwatch_timer
frame.start()
# stopwatch_timer.start()
