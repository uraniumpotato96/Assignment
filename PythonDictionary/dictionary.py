import json
import difflib
from difflib import get_close_matches
data = json.load(open('data.json'))
choice = False
choice2 = False
def findMeaning(w):
    if w in data:
        return(data[word])
    else:
        print ('invalid word is entered')
        print(' Or did you mean: %s' %get_close_matches(word,data.keys()))
        yn = input("press 'y' for YES and 'n' for NO ")
        yn = yn.casefold()
        if yn == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == 'n':
            return 'please enter the correct word'
        else:
            return('invalid option is selected!!')

while( choice != True):
    choice = False
    choice2 = False
    word = input("Enter the word to be searched ")
    word = word.casefold()
    word = findMeaning(word)
    if type(word) == list:
        for item in word:
            print(item)
    else:
            print(word)
    while(choice2 != True):
        c = input('wanna search more words?? y/n ')
        if c == 'y':
            choice = False
            choice2 = True
        elif c == 'n':
            choice = True
            choice2 = True
        else :
            print("invalid option please select again")
            choice2 = False
