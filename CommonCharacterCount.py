"""Given two strings, find the number of common characters between them.
Example
For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c".
"""


def commonCharacterCount(s1, s2):
    result = []
    list1 = [s for s in s1]
    list2 = [s for s in s2]
    for i in range(len(list1)):
        if list1[i] in list2:
            list2.remove(list1[i])
            result.append(list1[i])
    return len(result)