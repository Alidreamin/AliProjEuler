#!/usr/bin/env python

from time import clock
from math import sqrt
import itertools

start = clock()
"""
Pentagonal numbers are generated by the formula, P(n)=n(3n-1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
and D = |Pk - Pj| is minimised; what is the value of D?
"""
#########################################################
# try all combinations of pentagonal numbers?
# analytical way of solving?

# let's do some rough guessing first
#  we'll generate the first x pentagonal numbers
#  then take pair wise combination to determine D


def is_pen(num):
    n = (sqrt(24*num + 1) + 1)/6
    if n > 0 and n.is_integer():
        return n
    else:
        return False

pen_nums = []
for n in range(1, 5000):
    pen_nums.append(n*(3*n-1)/2)

print pen_nums
d = []


for tup in itertools.combinations(pen_nums, 2):
    add = is_pen(tup[0] + tup[1])
    sub = is_pen(abs(tup[0]- tup[1]))
    if (add) and (sub):
        d.append(abs(tup[0]-tup[1]))



print min(d)


# the above solution may happen upon D, but there's no guarantee
# we need to take advantage of the some mathematical certainty of the sequence
#






###############################################
stop = clock()
print("running time is %s" % (stop-start))

