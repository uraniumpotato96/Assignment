""""
In this game we will add a counter for how many guesses the user can have.

The counter is initial set to zero.

The while loop will run as long as the guesses are less to 5.

If the user guess the right number before that, the script will break and
present the user with how many guesses it took to guess the right number.

The variables in this script can be changed to anything.
"""

from random import randint

z = randint(1,10)
chance = 1
flag =  False
while(chance <= 5):
	num = int(input("Enter a number!"))
	if(num == z):
		print("you have guessed the right number in "+str(chance)+" chances.")
		flag = True
		break
	else:	
		print("You have "+str(5-chance)+" chances left.")	
		chance +=1

if(flag == False):
	print("The number to be guessed was " + str(z))
