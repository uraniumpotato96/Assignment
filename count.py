"""
	Function to count the unique elements present in an array.
"""
def count(lis):
    i=0
    for j in range(1,len(lis)):
        if lis[i] != lis[j]:
            i+=1
            lis[i]=lis[j]
    return i+1




print(count([1,1,1,1,1,1,1,1,1,1,2,3,4,5,6,7,123,12,56]))
