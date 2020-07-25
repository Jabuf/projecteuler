"""
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from locals import *

already_found = {1: 1}


def solution():
    n = 3
    longest_chain = 0
    longest_number = 0

    # If n is even, then produce_chain(2n) > produce_chain(n)
    # Hence why we do not need to compute the first half of the even numbers
    while n < 500000:
        chain_size = produce_chain(n)
        if chain_size > longest_chain:
            longest_chain = chain_size
            longest_number = n
        n += 2

    while n < 10 ** 6:
        chain_size = produce_chain(n)
        if chain_size > longest_chain:
            longest_chain = chain_size
            longest_number = n
        n += 1

    return [longest_number, longest_chain]


def produce_chain(starting_number):
    n = int(starting_number)

    if already_found.__contains__(n):
        return already_found[n]

    if n % 2 == 0:
        already_found[n] = 1 + produce_chain(n / 2)
    else:
        already_found[n] = 2 + produce_chain((3 * n + 1) / 2)

    return already_found[n]


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
