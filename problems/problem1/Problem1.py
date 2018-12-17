"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
from locals import *


def solution():

    sum_of_multiples = 0

    for i in range(0, 1000):
        if is_multiple_of(i, 3) or is_multiple_of(i, 5):
            sum_of_multiples += i
    return sum_of_multiples


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))