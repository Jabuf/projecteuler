from math import *

from numpy import *


def is_multiple_of(x, y):
    """ Return true if x is a multiple of y, false otherwise """
    try:
        return x % y == 0
    except ZeroDivisionError:
        return False


def is_even(x):
    """ Return true if x is even, false otherwise """
    return is_multiple_of(x, 2)


def is_prime(x):
    """ Return true is x is prime, false otherwise """

    if x == 1:
        return False

    primes = []
    next_prime = find_next_prime(primes)
    prime = False
    root = sqrt(x)

    while not prime:
        if next_prime > root:
            return True
        elif is_multiple_of(x, next_prime):
            return False
        else:
            next_prime = find_next_prime(primes)
            primes += [next_prime]


def find_next_prime(primes):
    """ Return the bigger prime closest to the ones in parameter """

    try:
        next_number = primes[len(primes) - 1] + 1
        found = False
    except IndexError:
        return 2

    while not found:

        i = 0
        root = sqrt(next_number)

        while not is_multiple_of(next_number, primes[i]):

            if primes[i] > root:
                return next_number
            elif (len(primes) - 1) == i:
                break
            else:
                i += 1

        next_number += 1
