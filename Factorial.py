"""Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""

def fib(num):
    if num ==0:
        return 1
    else:
        return num * fib(num-1)

a = list(raw_input("Enter the numbers seperated by ','\n").split(','))
b=[]
for i in a:
    b.append(fib(int(i)))
for i in b:
    print i ,','