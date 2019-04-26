"""Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
"""
def isLucky(n):
    numbers = [int(s) for s in str(n)]
    firstsum = 0
    secondsum = 0
    for i in range(len(numbers)/2):
        firstsum = firstsum+numbers[i]
    for i in range(len(numbers)/2,len(numbers)):
        secondsum = secondsum + numbers[i]
    return firstsum == secondsum
