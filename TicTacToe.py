positions=['1','2','3','4','5','6','7','8','9']
chance = True
gamestate = True
player1 = 'X'
player2 = 'O'
previousInputs = []
def printBoard(a):
    print ('------------')
    print ('|{0}|{1}|{2}|\n'.format(a[0],a[1],a[2]))
    print ('|{0}|{1}|{2}|\n'.format(a[3],a[4],a[5]))
    print ('|{0}|{1}|{2}|\n'.format(a[6],a[7],a[8]))
    print('-------------')
printBoard(positions)
def winCheck(a):
    if a[0] == a[1] == a[2] == player1 or a[3]==a[4]==a[5]==player1 or a[6]==a[7]==a[8]==player1 or a[0] == a[3] == a[6] == player1 or a[1] == a[4]== a[7] ==player1 or a[2] == a[5] == a[8] ==player1 or a[0] == a[4] == a[8] == player1 or a[2] == a[4] == a[6] == player1:
        return 1
    if a[0] == a[1] == a[2] == player2 or a[3]==a[4]==a[5]==player2 or a[6]==a[7]==a[8]==player2 or a[0] == a[3] == a[6] == player2 or a[1] == a[4]== a[7] ==player2 or a[2] == a[5] == a[8] ==player2 or a[0] == a[4] == a[8] == player2 or a[2] == a[4] == a[6] == player2:
        return 2
    if len(previousInputs) == 9:
        return 3
def updateBoard(a,choice):
    if a not in previousInputs and a in range(1,10):
        previousInputs.append(a)
        if choice:
            positions[a-1] = player1
            printBoard(positions)
        else:
            positions[a-1] = player2
            printBoard(positions)
    else:
        print 'please select a valid position.'
        printBoard(positions)
        return 2

while gamestate:
    try:
        number = int(input('Please mark a spot \n'))
        if updateBoard(number,chance) != 2:
            chance = not(chance)
        if(winCheck(positions) == 1):
            print'player one wins the game'
            gamestate = False
        if(winCheck(positions) == 2):
            print 'player Two wins the game.'
            gamestate = False
        if winCheck(positions) == 3:
            print 'It is a draw'
            gamestate = False
    except:
        print 'please provide a valid input'
