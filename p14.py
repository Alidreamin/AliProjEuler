#!/usr/bin/env python

from time import clock
from math import sqrt
"""
The following iterative sequence is defined for the set of positive integers:

n n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
start = clock()


max_length = 0
max_number = 0

for initial_number in range(1000000, 1, -1):
    next = 0
    length = 0
    current = initial_number
    #print initial_number
    while next != 1:
        if current % 2 == 0:
            next = current / 2
            current = next
        else:
            next = current * 3 + 1
            current = next
        length += 1
    if length > max_length:
        max_length = length
        max_number = initial_number


print max_number




stop = clock()
print("running time is %s" % (stop-start))

