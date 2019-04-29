"""Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""

def addBorder(picture):
    output = []
    output.append('*'*(len(picture[0])+2))
    for i in picture:
        output.append('*'+i+'*')
    output.append('*' * (len(picture[0]) + 2))
    return output
