'''Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''

command = ''
while True:
    command = raw_input("Enter the option\n").lower()
    if(command == "help"):
        print "start"
        print 'stop'
        print 'quit'
    elif(command == 'start'):
        print("the car has started")
    elif(command == 'stop'):
        print("the car has stopped")
    elif(command == 'quit'):
        break
    else:
        print "invalid input"
