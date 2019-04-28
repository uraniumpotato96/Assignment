import string
def encrypt(text,shift):
    #create a string that contains all alphabets.
    alphabet = string.ascii_lowercase
    #create a shifted version of the original string.
    shifted = alphabet[shift:]+alphabet[:shift]
    encrpytedList= list(range(len(text)))

    for i,char in enumerate(text.lower()):
        if char in alphabet:
            originalIndex = alphabet.index(char)
            newLetter = shifted[originalIndex]
            encrpytedList[i]=newLetter
        else:
            encrpytedList[i]=char
    return ''.join(encrpytedList)



def decrypt(text,shift):
        alphabet = string.ascii_lowercase
        shifted = alphabet[shift:]+alphabet[:shift]
        dlist = list(range(len(text)))
        for i,char in enumerate(text.lower()):
            if char in shifted:
                originalIndex=shifted.index(char)
                newLetter=alphabet[originalIndex]
                dlist[i]=newLetter
            else:
                dlist[i]=char
        return ''.join(dlist)

encryptedText = encrypt(input('enter the message to be encrypted:\n'),int(input('Enter the shift index:\n')))
print('The cipher text is : ' + encryptedText)
decryptedText = decrypt(encryptedText,int(input('Enter the shift index used for the encryption process.\n')))
print('The original message is : ' + decryptedText)
