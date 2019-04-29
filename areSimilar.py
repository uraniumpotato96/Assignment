"""Two arrays are called similar if one can be obtained from another by swapping at most one pair
 of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.
"""


def areSimilar(A, B):
    r = []
    for i in range(len(A)):
        if A[i] != B[i]:
            r.append([A[i], B[i]])

    if len(r) == 0 or len(r) == 2 and r[0] == r[1][::-1]:
        return True
    return False