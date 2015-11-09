#!/usr/bin/python

import re

#file_handle = open( '/home/gsmyth/regex_sum_42.txt' )
file_handle = open( 'regex_sum_196416.txt' )
numlist = list()

for line in file_handle:
    line = line.rstrip()
    numbers = re.findall( '[0-9]+', line )
    if len( numbers ) == 0 :
        continue


    numlist.append( sum( int(x) for x in numbers ))

print sum( numlist )
