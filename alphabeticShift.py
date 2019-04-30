"""

Given a string, replace each of its character by the next one in the English alphabet (z would be replaced by a).

Example

For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".

"""

import string
def alphabeticShift(text):
    alphabet = string.ascii_lowercase
    shifted = string.ascii_lowercase[1:]+string.ascii_lowercase[:1]
    encrpytedList= list(range(len(text)))

    for i,char in enumerate(text.lower()):
        if char in alphabet:
            originalIndex = alphabet.index(char)
            newLetter = shifted[originalIndex]
            encrpytedList[i]=newLetter
        else:
            encrpytedList[i]=char
    return ''.join(encrpytedList)
