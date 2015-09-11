#!/usr/bin/python

"""
We can use loops to simulate natural processes over time. 
Write a program that calculates the populations of two kinds of wumpuses over time. 
At the beginning of year 1, there are 1000 slow wumpuses and 1 fast wumpus. 
This one fast wumpus is a new mutation. 
Not surprisingly, being fast gives it an advantage, as it can better escape from predators. 
Each year, each wumpus has one offspring. 
(We'll ignore the more realistic niceties of sexual reproduction, like distinguishing males and females.). 
There are no further mutations, so slow wumpuses beget slow wumpuses, and fast wumpuses beget fast wumpuses. 
Also, each year 40% of all slow wumpuses die each year, while only 30% of the fast wumpuses do.

So, at the beginning of year one there are 1000 slow wumpuses. Another 1000 slow wumpuses are born. 
But, 40% of these 2000 slow wumpuses die, leaving a total of 1200 at the end of year one. 
Meanwhile, in the same year, we begin with 1 fast wumpus, 1 more is born, and 30% of these die, leaving 1.4. 
(We'll also allow fractional populations, for simplicity.)

Beginning of Year	Slow Wumpuses	Fast Wumpuses
1	                1000	                1
2	                1200	                1.4
3	                1440	                1.96

Enter the first year in which the fast wumpuses outnumber the slow wumpuses. 
Remember that the table above shows the populations at the start of the year.
"""

"""
 Args : slow lifecycle, fast lifecycle
"""
def wumpuses( slow, fast ) :
	year = 1
	while fast < slow:
		slow *= 2
		slow *= 0.6

		fast *= 2
		fast *= 0.7

		year += 1
                print "Slow: ", slow, " Fast : ", fast, " Year : ", year
        print "Final Slow: ", slow, " Fast : ", fast, " Year : ", year

wumpuses ( 1000, 1 )
