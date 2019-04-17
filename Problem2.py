""""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
a = []
flag = False
try:
    n = int(input("Enter the number of elements\n"))
    for i in range(n):
        a.append(int(input()))
    target = int(input("Enter the target to be matched"))
    if (len(a) > 2):
        for i in range(1,len(a)):
            num = a[i]
            second = target - num
            if second in a:
                print a.index(second),a.index(num)
                flag = True
                break
        if flag == False:
            print "no combination adds up to the target"
    else:
        print "invalid operation"
except:
    print "Operation dosent work for non numbers"




