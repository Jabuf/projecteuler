"""
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from locals import *


def solution():
    sum_squares = 0
    sum_numbers = 0

    for i in range(1, 101):
        sum_squares += i * i
        sum_numbers += i

    return (sum_numbers * sum_numbers) - sum_squares


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
