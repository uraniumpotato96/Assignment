"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.

"""


def arrayMaximalAdjacentDifference(inputArray):
    i = 0
    diff = 0
    for j in range(1, len(inputArray)):
        tempDiff = abs(inputArray[i] - inputArray[j])
        if diff < tempDiff:
            diff = tempDiff
        i += 1

    return diff