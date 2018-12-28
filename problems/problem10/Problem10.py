"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from locals import *


def solution():
    a = 0
    b = 0
    c = 0

    found = False

    while not found:

        a += 1
        b = a + 1

        while not found:

            c = 1000 - (a + b)

            if a * a + b * b == c * c:
                found = True
            elif c == b or c < b:
                break
            else:
                b += 1

    return [a, b, c]


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
