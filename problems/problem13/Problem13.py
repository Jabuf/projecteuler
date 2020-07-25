"""
https://projecteuler.net/problem=13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

See Problem13Constants.py
"""

from locals import *
from problems.problem13.Problem13Constants import *


def solution():
    sum_50_digits = 0

    for i in range(0, len(NUMBERS_50_DIGITS)):
        sum_50_digits += NUMBERS_50_DIGITS[i]

    return str(sum_50_digits)[0:10]


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
