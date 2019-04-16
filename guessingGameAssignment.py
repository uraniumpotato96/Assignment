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
