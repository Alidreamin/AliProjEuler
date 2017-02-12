#!/usr/bin/env python

from time import clock
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
# must run in less than one minute time
# so far I have not been concerned with algorithmic efficiency
#


# so far I've just been trying to solve the problem in a run time of less than one minute (one minute run time is trivial to achieve)

#anyway, back to the problem


def check(number):
    #this method will check if the given positive number is even divisible by all of the numbers from 1 to 20

    for i in range(1, 20):
        if number%i != 0:
            break
            return False
    else:
        return True



# let's start marching upward and checking at each step
# we know that the number must be even.  what else can we say about it in an effort to reduce our computational burden?
# cannot be a prime.  but using that fact may introduce more complexity than needed
# we can start at 2520
start = clock() # to help figure out running time


smallest_number = 2520

while True:
    smallest_number += 2
    if check(smallest_number):
        print(smallest_number)
        break









end = clock()
print(end - start)
