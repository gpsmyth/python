#!/usr/bin/python
"""
Convert the following English description into code.

Initialize n to be 1000. Initialize numbers to be a list of numbers from 2 to n, but not including n.
With results starting as the empty list, repeat the following as long as numbers contains any numbers.
Add the first number in numbers to the end of results.
Remove every number in numbers that is evenly divisible by (has no remainder when divided by) the 
      number that you had just added to results.
How long is results?

To test your code, when n is instead 100, the length of results is 25.
"""

def get_prime ( n ) :
    results = []
    numbers = range(2, n)

    while numbers != []:
        results.append(numbers[0])
        numbers = [n for n in numbers if n % numbers[0] != 0]

    return len(results)

parm = int(raw_input("Number? "))
print get_prime ( parm )
