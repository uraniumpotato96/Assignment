""""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

while(True):
    try:
        n = int(input("Enter the number of elements\n"))
        a = []
        for i in range(n):
            a.append(int(input()))
        string = ''
        for i in a:
            string += str(i)
        num = int(string)+1
        output = []
        for i in str(num):
            output.append(int(i))
        print a,"\n",output
        break
    except:
        print "Invalid operation"
        continue