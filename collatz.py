#!/usr/bin/python
"""
The following iterative sequence is defined for the set of positive integers:

n goes to n/2 (n is even)
n goes to 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 to 40 to 20 to 10 to  5 to 16 to 8 to 4 to 2 to 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms
"""

global n 
n = 0

"""
http://projecteuler.net/problem=14
"""
global largest 
largest = 0

def collatz( n ) :
    global largest

    print str(n),
    if n > largest :
        largest = n

    if n == 1 :
        return n
    elif ( n % 2 == 0 ) :
        return collatz( n / 2 )
    else :
        return collatz(( n * 3 ) + 1 )

collatz_list = [23, 217, 13]
for i in collatz_list :
    print collatz( i )
    print "Largest is ", largest
    largest = 0
