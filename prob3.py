#!/usr/bin/env python

from math import sqrt
from time import clock
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

start = clock()
#first thought:
# generate all primes less than given number
# go through this list of primes and test which of these primes is the largest that is a divisor of the given number



#generate primes
prime_set = [2, 3]
limit = 600851475143
for potential_prime in range(3, int(sqrt(limit)), 2): #iterate over odd numbers from 3 to sqrt of limit...these are potential primes
    for x in range(2, int(sqrt(potential_prime))): # primality test
        if potential_prime%x == 0:
            break
    else:
        prime_set.append(potential_prime)



print(prime_set)







max = 1
for number in prime_set:
    if limit % number == 0:
        max = number
    print(max)

print(max)

stop = clock()
print(stop-start)