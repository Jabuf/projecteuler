"""
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from locals import *


def solution():
    n = 20
    return get_lattice_paths(n)


def get_lattice_paths(n):
    """ https://en.wikipedia.org/wiki/Lattice_path """
    return int(scipy.special.binom(2 * n, n))


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
