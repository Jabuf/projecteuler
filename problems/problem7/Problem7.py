"""
https://projecteuler.net/problem=6

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

from locals import *


def solution():
    numbers_of_primes = 0
    x = 0

    while numbers_of_primes < 10000:
        x += 1
        if is_prime(x):
            numbers_of_primes += 1

    return x


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
