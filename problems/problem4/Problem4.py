"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from locals import *


def solution():
    palindrome = 0

    for i in range(0, 999):
        for j in range(0, 999):

            current_product = i * j

            if is_palindrome(str(current_product)) and current_product > palindrome:
                palindrome = current_product

    return palindrome


with Timer() as timed:
    print(solution())
print("Seconds taken: {0}".format(timed.elapsed))
