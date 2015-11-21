#!/usr/binpython
"""
In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html 
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
Last name in sequence: Anayah
Actual problem: Start at: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Kinneil.html 
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: D
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

Sample execution

Here is a sample execution of a solution:

$ python solution.py 
Enter URL: http://pr4e.dr-chuck.com/ ... /known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Fikret.html
Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Montgomery.html
Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Mhairade.html
Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Butchi.html
Last Url: http://pr4e.dr-chuck.com/ ... /known_by_Anayah.html
The answer to the assignment for this execution is "Anayah".
"""
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
# This code is referenced from http://www.pythonlearn.com/code/urllinks.py

import urllib
from BeautifulSoup import *

def getTheUrl( url, process_count, posn_count ) :
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    i_count = 0
    tagStr = ""
    
    for tag in tags:
       i_count += 1
       if i_count == posn_count:
           tagStr = tag.get('href', None)

    return tagStr 

def main():
    process_i = 0

    url = raw_input('Enter URL : ')
    process_count = int ( raw_input('Enter count : '))
    posn_count = int ( raw_input('Enter position : '))
    while process_i < process_count:
        process_i += 1
        print "Retrieving: ", url
        url = getTheUrl( url, process_count, posn_count )
    print "Last Url: ", url

if __name__ == "__main__":
    main()

