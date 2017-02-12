#!/usr/bin/env python
from time import clock
from math import sqrt
import itertools
start = clock()

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
#####################################################################################################################

# cannot be larger than 9 digits, not including 0


# first generate all the pandigital numbers: all permuatations of 1 through 9 for a given n
# go from largest number down, check for primality
# stop at first found prime



def primality_test(potential_prime):
    for i in range(2, int(sqrt(potential_prime))+1):
        if potential_prime%i == 0:
            return False
            break
    else:
        return True



list = []
for n in range(9,3, -1):
    one_through_n = [x for x in range(1, n+1)]
    for number_list in itertools.permutations(one_through_n, n):
        #print n
        #print number_list
        num = int(''.join(map(str, number_list)))
        list.append(num)

list = sorted(list)

for a in reversed(list):
    if primality_test(a):
        print a
        break









######################################################################################################################

stop = clock()
print("running time is %s" % (stop-start))
# strict rule: running time < 1 minute
# goal: as efficient as possible


