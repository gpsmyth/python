#!/usr/bin/python
"""
 Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to 
http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, 
read the JSON data from that URL using urllib and then parse and extract the 
comment counts from the JSON data, compute the sum of the numbers in the file 
and enter the sum below:

We provide two files for this assignment. One is a sample file where we 
give you the sum for your testing and the other is the actual data 
you need to process for the assignment.

    Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2482)
    Actual data: http://python-data.dr-chuck.net/comments_196422.json (Sum ends with 66)

You do not need to save these files to your folder since your program will 
read the data directly from the URL. Note: Each student will have a distinct 
data url for the assignment - so only use your own data url for analysis.

Data Format

The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

The closest sample code that shows how to parse JSON and extract a list is json2.py. 
You might also want to look at geoxml.py to see how to prompt for a URL 
and retrieve data from a URL.

Sample Execution

$ python solution.py 
Enter location: http://python-data.dr-chuck.net/comments_42.json
Retrieving http://python-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2482

"""
import urllib
import json

url = raw_input('Enter Location - ')
print 'Retrieving ', url

html = urllib.urlopen(url).read()

"""
html makde explicit for initial testing
html = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.json').read()
"""

data = ""
for line in html:
    data += line

print 'Retrieved ', len( data ), ' characters'

jsonResponse = json.loads( html )
jsonData = jsonResponse["comments"]

print "Count: ", len( jsonData )

count = 0

for item in jsonData:
    count += int( item.get( 'count' ))

print 'Sum: ', count
