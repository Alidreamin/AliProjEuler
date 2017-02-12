#!/usr/bin/env python

from time import clock
from math import sqrt
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
 begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
 multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""
start = clock()

# let's apply python's built-on lexical comparison and python's built-in sorted() function

filename = '/Users/alisheikh/PycharmProjects/AliReelin/p022_names.txt'
with open(filename, "rt") as f:
    for line in f:
        unordered_list = line.split(',')

unordered_list = [x.strip('"') for x in unordered_list]





ordered_list = sorted(unordered_list)

print ordered_list






def worth(name, position):
    #given a string, returns the worth as described above
    sum = 0
    for letter in name:
        sum = sum + value_dict[letter]
    return sum * position


# create a dictionary that worth() can use to compute
from string import ascii_uppercase
count = 1
value_dict = {}
for letter in ascii_uppercase:
    value_dict[letter] = count
    count += 1

total_worth = 0
for index, name in enumerate(ordered_list):
    total_worth += worth(name,index+1)

print total_worth


stop = clock()
print("running time is %s" % (stop-start))

