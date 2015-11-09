import time

def date(month, day):
    """
    Given numbers month and day, returns a string of the form '2/12',
    with the month followed by the day.
    """
    return str( month ) + "/" + str(day )

def number_of_i(word):
    """Returns the number of lower-case i's in the word."""
    # return count("i", word )
    return word.count("i")

print date(2, 12)

print number_of_i( "misseditit" )

print time.strftime("%Y")
