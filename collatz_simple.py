# Collatz

def collatz(n):
    """Prints the values in the Collatz sequence for n."""

    i = n
    while i > 1:
        print i
        
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3 * i + 1
           
collatz(1000)
