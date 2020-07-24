from math import *
from numpy import *

primes = []  # the list of primes already found


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

    # We use a global list of primes to be more efficient when the function is called multiple times
    global primes

    if x in primes:
        return True

    root = sqrt(x)

    for i in range(0, len(primes)):
        if primes[i] > root:
            break
        if is_multiple_of(x, primes[i]):
            return False

    next_prime = find_next_prime(primes)
    prime = False
    while not prime:
        if next_prime > root:
            primes += [next_prime]
            return True
        elif is_multiple_of(x, next_prime):
            return False
        else:
            next_prime = find_next_prime(primes)
            primes += [next_prime]


def find_next_prime(previous_primes):
    """ Return the bigger prime closest to the ones in parameter """
    try:
        next_number = previous_primes[len(previous_primes) - 1] + 1
        found = False
    except IndexError:
        return 2

    while not found:

        i = 0
        root = sqrt(next_number)

        while not is_multiple_of(next_number, previous_primes[i]):

            if previous_primes[i] > root:
                return next_number
            elif (len(previous_primes) - 1) == i:
                break
            else:
                i += 1

        next_number += 1


def get_integer_decomposition(x):
    """ Return the integer decomposition of x """
    if is_prime(x) or x == 1:
        return [1, x]

    global primes

    for i in range(0, len(primes)):
        if is_multiple_of(x, primes[i]):
            return [primes[i], int(x / primes[i])]

    return [1, x]


def get_prime_decomposition(x, prime_decomposition=None):
    """ Return the prime decomposition of x """
    if prime_decomposition is None:
        prime_decomposition = []
    decomposition = get_integer_decomposition(x)

    first_factor = decomposition[0]
    second_factor = decomposition[1]

    # recursive call while both factors aren't primes numbers
    if not is_prime(first_factor) and first_factor != 1:
        get_prime_decomposition(first_factor)
    else:
        prime_decomposition += [first_factor]

    if not is_prime(second_factor) and second_factor != 1:
        get_prime_decomposition(second_factor, prime_decomposition)
    else:
        prime_decomposition += [second_factor]

    return prime_decomposition


def get_number_of_divisors(x):
    """ Return the number of divisors of x """
    if x == 1:
        return 1
    elif is_prime(x):
        return 2

    prime_decomposition = get_prime_decomposition(x)
    prime = prime_decomposition[0]
    power_of_primes = [1]  # this will contain the power of each different primes

    for i in range(1, len(prime_decomposition)):
        if prime != prime_decomposition[i]:
            prime = prime_decomposition[i]
            power_of_primes += [1]
        else:
            power_of_primes[len(power_of_primes) - 1] = power_of_primes[len(power_of_primes) - 1] + 1

    number_of_divisors = 1

    # the formula to get the number of divisors using the product of prime factors
    for i in range(0, len(power_of_primes)):
        number_of_divisors *= (power_of_primes[i] + 1)

    return number_of_divisors
