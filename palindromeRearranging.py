"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

"""

from collections import Counter as C
def palindromeRearrangin(a):
    b = list(C(a).values())

    hit = 0

    for i in b:
        if (i % 2) != 0:
            hit +=1
            if hit == 2:return False
    return True

print (palindromeRearrangin('malayalam'))


"""
logic
# count the number of each individual character
# can form a palindrome only if:
#  at most one of the character counts is odd, all others must be even
"""