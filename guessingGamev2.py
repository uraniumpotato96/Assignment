from random import randint
count = 1
randomNumber = randint(1, 100)
while True:
    number = int(input('Please guess a number.\n'))
    if(number < 1 or number > 100 ):
        print ('The number is out of bounds.')
        continue
    else:
        if number == randomNumber:
            print('You have guessed correctly in {0} chances.'.format(count))
            break
        elif abs(randomNumber - number) < 10 and count == 1 :
            previousGuess = randomNumber
            print ("Warm")
            count += 1
        elif abs(randomNumber - number) > 10 and count ==1:
            previousGuess = randomNumber
            print('Cold')
            count +=1
        elif abs(previousGuess -number)  < randomNumber:
            print 'warmer'
            count += 1
        elif abs(previousGuess - number) > randomNumber:
            print 'Colder'
            count += 1
        elif count == 10:
            print randomNumber
            break

