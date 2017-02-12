#!/usr/bin/env python

from time import clock
from math import sqrt

start = clock()
"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
#########################################################


first = [0,1,2,3,4,5,6,7,8,9]

import itertools

z = sorted(list(itertools.permutations(first, 10)))
print z[999999]


#I should try to implement the permutations function myself.  actually, better to implement a direct lexicographic function

# also the Steinhaus-Johnson-Trotter algorithm

# heap's algorithm






###############################################
stop = clock()
print("running time is %s" % (stop-start))

