#!/usr/bin/env python

from time import clock
from math import sqrt
import itertools
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.



As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which *cannot* be written as the sum of two abundant numbers.

"""
start = clock()

def is_abundant_number(num):
    sum = 0
    for i in range(1, int(num/2)+1):
        if num%i == 0:
            sum += i

    if sum > num:
        return True
    else:
        return False

abundant_nums = []

# idea:
#  create list of abundant numbers
for possible_abundant_number in range(12, 28123-11):
    if is_abundant_number(possible_abundant_number):
        abundant_nums.append(possible_abundant_number)


print(abundant_nums)



unique_sums_abundant_nums = set()
for subset in itertools.combinations_with_replacement(abundant_nums, 2):
    a_sum = subset[0] + subset[1]
    if a_sum not in unique_sums_abundant_nums:
        unique_sums_abundant_nums.add(a_sum)


all_pos_int_less_than_28123 = {x for x in range(1, 28124)}

difference_set = all_pos_int_less_than_28123 - unique_sums_abundant_nums

print(sum(difference_set))



 # go through all natural numbers from second smallest abundant number to 28123
 # for each number, check all combinations of abundant numbers less than the current number






# ya = []
# for x in range(1, 10):
#     ya.append(x)
#
# print ya
#
#
# for subset in itertools.combinations_with_replacement(ya, 2):
#     print subset
#     print subset[1] + subset[0]


stop = clock()
print("running time is %s" % (stop-start))

