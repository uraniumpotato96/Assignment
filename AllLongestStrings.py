"""Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""
def allLongestStrings(a):
    length = []
    result = []
    for i in a:
        length.append(len(i))
    maxLength = max(length)
    for i in a:
        if len(i) == maxLength:
            result.append(i)

    return result
