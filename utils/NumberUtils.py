
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
    prime = True
    y = x

    while prime:
        y -= 1

        if y < 1:
            prime = False
            break
        elif y == 1:
            break
        elif is_multiple_of(x, y):
            prime = False

    return prime


def find_next_prime(previous_prime):
    """ Return the closest bigger prime than the one in parameter """
    next_number = previous_prime + 1

    while not is_prime(next_number):
        next_number += 1

    return next_number
