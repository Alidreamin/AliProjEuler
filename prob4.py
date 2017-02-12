#!/usr/bin/env python

from time import clock
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


def is_palidromic_number(number):
    # first we convert number to list
    number_string = str(number)
    number_list = []
    for digit in number_string:
        number_list.append(int(digit))

    # now test if it's a palindromic number
    reversed_number_list = []
    for i in reversed(number_list):
        reversed_number_list.append(i)

    if number_list == reversed_number_list:
        return True
    else:
        return False



start = clock()
largest_pal = 0
num_unique_multiplies = 0

for x in range(100, 999):
    for y in range(x, 999):
        z = x * y
        if is_palidromic_number(z):
            if z > largest_pal:
                largest_pal = z


print(largest_pal)

stop = clock()
print(stop-start)
