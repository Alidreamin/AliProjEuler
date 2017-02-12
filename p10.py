#!/usr/bin/env python

from time import clock
from math import sqrt
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million

"""
start = clock()

#generate primes
prime_set = [2]
limit = 2000000
for potential_prime in range(3, limit, 2): #iterate over odd numbers from 3 to limit...these are potential primes
    for x in range(2, int(sqrt(potential_prime))+1): # primality test
        if potential_prime % x == 0:
            break
    else:
        prime_set.append(potential_prime)

#print(prime_set)
print(sum(prime_set))
stop = clock()
print("running time is %s" % (stop-start))

# the trial division technique run time is ~ 30 seconds
# the time complexity is of the order n^1.5
# let's try the sieve of eratosthenes
# my inital guess is that we'll use set or list comprehensions
#

