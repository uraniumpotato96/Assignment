"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one.
Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
"""


def arrayChange(inputArray):
    moveCount = 0
    currentValue = inputArray[0]
    for i in range(0, len(inputArray) - 1):
        if (inputArray[i + 1] <= currentValue):
            moveCount += currentValue - inputArray[i + 1] + 1
            currentValue += 1
        else:
            currentValue = inputArray[i + 1]
    return moveCount
