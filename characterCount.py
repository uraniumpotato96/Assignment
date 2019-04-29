"""
    Write a function to count the number of characters that are present in a string.And return a dictionary which shows the
    count of all characters present in the given sentence.
"""

def countCharacters(sentence):

    output = {}

    for i in sentence:
        if i in output:
            output[i] +=1
        else:
            output[i] = 1
    return output
print countCharacters('abcdeacdhggh')