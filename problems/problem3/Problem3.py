"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from locals import *


def solution(x):
    largest_prime_found = 0
    first_prime = 2
    biggest_prime = first_prime
    primes = [first_prime]
    root = sqrt(x)

    while biggest_prime < root:
        biggest_prime = primes[len(primes) - 1]
        if is_multiple_of(x, biggest_prime):
            largest_prime_found = biggest_prime
        primes += [find_next_prime(primes)]

    return largest_prime_found


with Timer() as timed:
    print(solution(600851475143))
print("Seconds taken: {0}".format(timed.elapsed))
