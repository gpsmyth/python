"""
Clone of 2048 game.
"""

#import poc_2048_gui        
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
SIMULATION = 1
UNIT_TESTING = 0

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    if UNIT_TESTING:
        print '@ merge fn, line: ', line
    # At this stage, we first filter out all the 0 values,
    # Then when we find the next two numbers the same we
    # double the vaule of tiles[idx - 1] and make tiles[idx] 
    # equal to zero
    # tiles = filter(None, line)
    ## tiles = filter(lambda x: x != 0, line)
    # list comprehension
    tiles = [x for x in line if x != 0]
    for idx in range(1, len(tiles)):
        if tiles[idx - 1] == tiles[idx]:
            tiles[idx - 1] <<= 1
            tiles[idx] = 0

    # At this stage, we again filter out all the zeros
    # and then append the list with zeros.
    # tiles = filter(None, tiles)
    # tiles = filter(lambda x: x != 0, tiles)
    tiles = [x for x in tiles if x != 0]
    tiles.extend([0] * (len(line) - len(tiles)))

    if UNIT_TESTING:
        print 'Output of merged line', tiles
    return tiles


class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    INFO_LEVEL = 10
    TERSE_LEVEL = 20
    DEBUG_LEVEL = 30
    DEBUG = 0

    def __init__(self, grid_height, grid_width):
        self._rowsize = grid_height
        self._colsize = grid_width

        # Convert a numeric to a list
        self._rows = range( grid_height )
        self._cols = range( grid_width )
        self._dir_dict = {UP: 'up', DOWN: 'down', LEFT: 'left', RIGHT: 'right'}
        
        self._grid = self.reset()

        if SIMULATION: 
            for dummy in range(5):
                self.new_tile()
        #print self._grid.__str__()
        #print self.__str__()
        
        TwentyFortyEight.DEBUG = TwentyFortyEight.INFO_LEVEL
        #print self._grid.__str__()
        print self.__str__()

        up_list, down_list = [], []
        left_list, right_list = [], []

        for dummy_col in self._cols:
            # (( ... )) is used within append so as to make append see just 
            #  one arg
            #     otherwise a compile argument is thrown
            up_list.append(( 0, dummy_col ))
            down_list.append(( self._rowsize - 1, dummy_col ))
        for dummy_row in self._rows:
            left_list.append(( dummy_row, 0 ))
            right_list.append(( dummy_row, self._colsize - 1 ))
   
        self._tiles = {UP:up_list, DOWN:down_list,
                              LEFT:left_list, RIGHT:right_list}
        print "boundary tiles", self._tiles

    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # self._grid = map(lambda dummy: [0] * self._colsize, self._rows)

        # pylint complains about map unfortunately
        #_grid = map(lambda dummy: [0] * self._colsize, self._rows)
        _grid = [[0] * self._colsize for _ in range(self._rowsize)]

        return _grid
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        TwentyFortyEight.DEBUG = TwentyFortyEight.TERSE_LEVEL
        grid_str = ""
        #for row in range(self._rows):
        for row in self._rows:
            if TwentyFortyEight.DEBUG == TwentyFortyEight.TERSE_LEVEL:
                grid_str += str( self._grid[row] )
                grid_str += '\n'
            else:
                grid_str = '\n'.join( [ grid_str, str(self._grid[row]) ])
        return grid_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._rowsize 
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._colsize 
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        print 'Moving', self._dir_dict[direction] 
        
        #constants = [ "none", "up", "down", "left", "right" ]
        #constant_dic = dict([(c, i) for i, c in enumerate(constants)])
        #print 'Moving line ', constant_dic[direction]

        offset = OFFSETS[direction]
        tiles  = self._tiles[direction]
        line_len = self._colsize if offset[1] else self._rowsize

        for tile in tiles:
            grid_line = []
            for count in range( line_len ):
                grid_line.append( self._grid[tile[0] + offset[0] * count]
                                            [tile[1] + offset[1] * count])
            # TwentyFortyEight.DEBUG = TwentyFortyEight.DEBUG_LEVEL
            if TwentyFortyEight.DEBUG == TwentyFortyEight.DEBUG_LEVEL:
                print 'grid line detected before merge is ', grid_line

            grid_line = merge( grid_line )
            if TwentyFortyEight.DEBUG == TwentyFortyEight.DEBUG_LEVEL:
                print 'grid line after before merge is ', grid_line
            for count in range( line_len ):
                ( self._grid[tile[0] + offset[0] * count]
                            [tile[1] + offset[1] * count]) = grid_line[count]
        self.new_tile()

        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # a list comprehension is been creaed here, and the expression is 
        # creating a tuple of (row, col)
        # enumerate's first arg is a sequence; in this case of type list
        # enumerate() returns a tuple
        if TwentyFortyEight.DEBUG == TwentyFortyEight.INFO_LEVEL:
            for row, line in enumerate(self._grid):
                print 'Enumerated', row, line
                print type(line)
            
                # >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
                # >>> list(enumerate(seasons))
                # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
                # >>> list(enumerate(seasons, start=1))
                # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
            

        empty_tiles = [(row, col) for row, line in enumerate(self._grid) \
            for col, val in enumerate(line) if val == 0]
        if empty_tiles:
            row, col = random.choice(empty_tiles)
            self._grid[row][col] = 2 if random.random() < .9 else 4
        else:
            print 'No more empty tiles left\n'
        # print empty_tiles, note that both () and \ works here.
        # just need to make sure that no continuation character occurs after \
        # though
        if TwentyFortyEight.DEBUG == TwentyFortyEight.INFO_LEVEL:
            print 'row', row, ' col', col, \
                    ' has value self._grid[row][col] = ', \
                    self._grid[row][col] 
            print ( 'row', row, ' col', col, \
                    ' has value self._grid[row][col] = ', 
                    self._grid[row][col] )
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self._grid[row][col]
 
    
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
if SIMULATION: 
    GAME = TwentyFortyEight(4, 4)

    GAME.move(UP)
    GAME.move(LEFT)
    GAME.move(RIGHT)
    GAME.move(UP)
    GAME.move(DOWN)
    GAME.move(LEFT)
    GAME.move(UP)
    GAME.move(DOWN)
    GAME.move(RIGHT)
    GAME.move(RIGHT)

if UNIT_TESTING:
    LINEGRID = [2, 2, 0, 0]
    merge (LINEGRID)
    print "======================="

    LINEGRID = [0, 0, 2, 2]
    merge (LINEGRID)
    print "======================="

    LINEGRID = [0, 2, 2, 0]
    merge (LINEGRID)
    print "======================="

    LINEGRID = [0, 2, 0, 2]
    merge (LINEGRID)
    print "======================="

    LINEGRID = [2, 0, 2, 2]
    merge (LINEGRID)
    print "======================="

    LINEGRID = [2, 0, 2, 4]
    merge (LINEGRID)
    print "======================="

    LINEGRID = [2, 2, 2, 2]
    merge (LINEGRID)
    print "======================="

    LINEGRID = [2, 2, 2, 0]
    merge (LINEGRID)
    print "======================="

    LINEGRID = [2, 2, 4, 4]
    merge (LINEGRID)
    # print LINEGRID[::-1]
    print "======================="

    LINEGRID = [8, 16, 16, 8]
    merge (LINEGRID)
    # [start:stop:step] so step is -1
    # print LINEGRID[::-1]
    print "======================="

    LINEGRID = [0, 0, 0, 0]
    merge (LINEGRID)
    print "======================="

    LINEGRID = [4, 4, 4, 0]
    merge (LINEGRID)
    # L =  merge (LINEGRID)
    # L.reverse()
    # print 'reversed ', L
    print "======================="
