#!/usr/bin/env python

from time import clock
from math import sqrt
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

d(i) = t
d(t) = i

"""
start = clock()


def sum_of_divisors(number):
    sum = 0
    for x in range(1, int(number/2)+1):
        if number%x == 0:
            sum += x
    print "the sum for ", number, "is ", sum
    return sum

amicable_numbers = []
i = 2

while i < 10000:
    if i not in amicable_numbers:
        #print i
        test = sum_of_divisors(i)
        check = sum_of_divisors(test)
        if check == i and i != test:
            print "ding"
            amicable_numbers.append(i)
            if test not in amicable_numbers:
                amicable_numbers.append(test)
        i+=1
    else:
        i+=1

print amicable_numbers
print sum(amicable_numbers)







stop = clock()
print("running time is %s" % (stop-start))

