#!/usr/bin/env python
from time import clock
from math import sqrt
import itertools
start = clock()

"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
#####################################################################################################################



#
number_ways = 0
for n in range(2,100):
    one_through_100 = [x for x in range(1, 102-n)]  # list of integers from 1 to 100
    for number_tuple in itertools.combinations_with_replacement(one_through_100, n):
        if sum(number_tuple) == 100:
             print number_tuple
             number_ways += 1
             print number_ways

#  i feel that some recursive call to a function will be the fastest solution
#




#  can I use a partition generating function?











######################################################################################################################

stop = clock()
print("running time is %s" % (stop-start))
# strict rule: running time < 1 minute
# goal: as efficient as possible


