"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from locals import *

TWO_MILLIONS = 2000000


def solution():
    current_prime = 2
    sum_primes = 0
    primes = [current_prime]

    while current_prime < TWO_MILLIONS:
        sum_primes += current_prime
        current_prime = find_next_prime(primes)
        primes.insert(len(primes), current_prime)

    return sum_primes


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
