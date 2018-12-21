"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from locals import *


def solution():
    answer_found = False
    smallest_number = 2520

    while not answer_found:
        smallest_number += 2520
        answer_found = is_evenly_divisible(smallest_number)

    return smallest_number


def is_evenly_divisible(x):
    for i in range(1, 20):
        if not (x % i == 0):
            return False
    return True


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
