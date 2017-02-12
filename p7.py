#!/usr/bin/env python
from math import sqrt
from time import clock

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
start = clock()

#generate primes until index 10001 is reached
prime_set = [2, 3] #initialize prime number set
index = 1
potential_prime = 3

while index != 10000:
    potential_prime += 2
    for x in range(2, int(sqrt(potential_prime))+1): # primality test
        if potential_prime%x == 0:
            break #break from primality test
    else:
        prime_set.append(potential_prime)
        index += 1

print(int(sqrt(49)))
print(index)
print(prime_set)
print(prime_set[10000])
print(len(prime_set))
stop = clock()

print("running time is %s" % (stop-start))
