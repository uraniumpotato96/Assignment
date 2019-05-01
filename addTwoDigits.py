"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.
"""


def addTwoDigits(n):
    return int(str(n)[0]) + int(str(n)[1])
