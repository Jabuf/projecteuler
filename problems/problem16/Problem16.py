"""
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from locals import *


def solution():
    x = 2 ** 1000
    sum_digits = 0
    x_s = str(x)

    for i in range(0, len(x_s)):
        sum_digits += int(x_s[i])

    return sum_digits


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
