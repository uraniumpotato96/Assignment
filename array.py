"""
	Program to find whether the contents of array 1 are present as squares of the same number but in different order in  the array 2.

example

array1:[1,2,3,4]
array2:[16,9,1,4]
output:True
"""
arr1=[1,4,4,1]
arr2=[1,1,16,16]

def same(ar1,ar2):
    if len(ar1) != len(ar2):
        return False
    else:
        for i in ar1:
            try:
                ch = ar2.index(i**2)

            except:
                return False
            print(ar2)    
            arr2.pop(ch)
        return True

print(same(arr1,arr2))
