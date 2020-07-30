"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

from locals import *


def solution():
    primes_found = []

    while len(primes_found) < 10001:
        primes_found += [find_next_prime(primes_found)]

    return primes_found[len(primes_found)-1]


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
