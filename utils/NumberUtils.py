from math import *

from numpy import *


def is_multiple_of(x, y):
    """ Return true if x is a multiple of y, false otherwise """
    multiple_of = False
    if y != 0:
        multiple_of = x % y == 0

    return multiple_of


def is_even(x):
    """ Return true if x is even, false otherwise """
    return is_multiple_of(x, 2)


def is_prime(x):
    """ Return true is x is prime, false otherwise """

    prime = False
    root = sqrt(x)
    first_prime = 2
    primes = [first_prime]
    next_prime = first_prime

    while not prime:
        if x == 1:
            break
        if is_multiple_of(x, next_prime):
            break
        elif next_prime > root:
            prime = True
            break
        else:
            next_prime = find_next_prime(primes)
            primes += [next_prime]

    return prime


def find_next_prime(primes):
    """ Return the bigger prime closest to the ones in parameter """

    next_number = primes[len(primes) - 1]
    found = False

    while not found:

        i = 0
        next_number += 1
        root = sqrt(next_number)

        while not is_multiple_of(next_number, primes[i]) and not found:
            if primes[i] > root:
                found = True
                break
            elif (len(primes) - 1) == i:
                break
            else:
                i += 1

    return next_number
