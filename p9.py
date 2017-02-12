#!/usr/bin/env python

from time import clock
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
start = clock()
# two constraints:  one is that a + b + c = 1000
# the other is that a^2 + b^2 = c^2

# two equations, three unkowns, so we cannot solve analytically, obviously
#

# 5 < c < 998
# 2 < b < 499
# 1 < a < 994

# do an exhaustive search?  without knowing any properties of pythagorean triplets that will short cut the solution, can we make this easier?
#
#

for possible_c  in range(1, 998):
    for possible_b in range(2,499):
        for possible_a in range(1, 300):
            if ((possible_a + possible_b + possible_c == 1000)  and (pow(possible_a,2) + pow(possible_b,2) == pow(possible_c,2))):
                print(possible_b*possible_a*possible_c)
                break




stop = clock()
print("running time is %s" % (stop-start))
# this is waaaaay too slow!
# come back to this and make it better