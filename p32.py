#!/usr/bin/env python
from time import clock
from math import sqrt
import itertools
start = clock()

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
#####################################################################################################################


# brute force technique:
# generate all of the 1-9 pandigital numbers

list = []
for n in range(9,3, -1):
    one_through_n = [x for x in range(1, n+1)]
    for number_list in itertools.permutations(one_through_n, n):
        num = int(''.join(map(str, number_list)))
        list.append(num)











######################################################################################################################

stop = clock()
print("running time is %s" % (stop-start))
# strict rule: running time < 1 minute
# goal: as efficient as possible

