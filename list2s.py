#!/usr/bin/python
"""
Turn the following English description into code:

Create a list with two numbers, 0 and 1, respectively.
For 40 times, add to the end of the list the sum of the last two numbers.
What is the last number in the list?

To test your code, if you repeat 10 times, rather than 40, your answer should be 89.

This process computes Fibonacci numbers. Since 0 and 1 are considered the 0th and 1st Fibonacci numbers, 
respectively, we effectively asked you to give the 41st Fibonacci number. 
While a simple and seemingly arbitrary computation, the Fibonacci sequence appears repeatedly in mathematics and nature.
"""

my_list = [0, 1]
parm = 0

for i in range( 0, 40 ) :
    parm = sum( my_list[ -2: ] )
    assert isinstance( parm, object )
    my_list.append( parm )
    #print my_list
    #i += 1

print parm

# Another way without lists
x = 0
y = 1
for i in range( 40 ) :
    x, y = y, x+ y
print y
