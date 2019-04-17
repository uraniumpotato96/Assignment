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




