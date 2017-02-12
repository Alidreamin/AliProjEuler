#!/usr/bin/env python
from time import clock
from math import sqrt
import itertools
start = clock()

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit
fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
#####################################################################################################################

from decimal import *


def principal_period(s):
    #this method takes a string,
    # concatenates it to itself
    # the find method is applied, looking for s within s+s from beg index = 1 (the second spot from the left)
    # to end index = -1 (-1 is the end of a string)

    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]  #if i = -1 means that it simply found the full orginal string again, no pattern


max = 0
decimal = 'none'
pat = 'none'

# getcontext().prec = 70000  #is there a mathematical fact that determine the minimum precision required?
# for d in range (2, 1000):
#     # print 1.0/d
#     # print format(1.0/d, '.99g')
#     # print Decimal(1.0)/Decimal(d)
#     decimal_portion = str(Decimal(1.0)/Decimal(d))[2:]
#     possible_pattern = principal_period(decimal_portion)
#     #print decimal_portion
#     #print possible_pattern
#     if possible_pattern != None:
#         if len(possible_pattern) > max:
#             pat = possible_pattern
#             max = len(possible_pattern)
#             decimal = d




# print "longest is %s" % decimal
# print Decimal(1.0)/Decimal(decimal)
# print pat

print principal_period('0133133133')



#  the pattern can beging after a few non repeating digits!!

######################################################################################################################

stop = clock()
print("running time is %s" % (stop-start))
# strict rule: running time < 1 minute
# goal: as efficient as possible

