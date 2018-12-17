"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
from locals import *


def solution():

    sum_of_even = 2
    first_number = 1
    second_number = 2

    while sum_of_even < 4000000:
        next_number = first_number + second_number
        if is_even(next_number):
            sum_of_even += next_number

        first_number = second_number
        second_number = next_number

    return sum_of_even


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))