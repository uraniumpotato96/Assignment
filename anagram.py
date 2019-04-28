"""
Program to find if two strings are anagrams of each other.
example 
sentence1:MAM
sentence2:MAM
output: TRUE
"""
def anagram():
    print("Enter 2 strings to check if they are anagrams of each other.")
    str1= input("Enter the first string.")
    str2 = input('Enter the second string.')
    c1={}
    c2={}
    for i in str1 :
        c1[i] = str1.count(i)
    for j in str2:
        c2[j]=str2.count(j)
    return c1==c2
print(anagram())
