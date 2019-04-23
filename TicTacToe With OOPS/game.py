from TTT import GameTicTacToe

gameObj = GameTicTacToe()
gameObj.printBoard()
chance = True

while gameObj.gamestate:
    try:
        number = int(input('Please mark a spot \n'))
        if gameObj.updateBoard(number,chance) != 2:
            gameObj.printBoard()
            chance=not(chance)
        if gameObj.winCheck() == 1:
            print('Player One Wins the game!!!')
            gameObj.gamestate = False
        if gameObj.winCheck() == 2:
            print('Player Two Wins The Game!!!')
            gameObj.gamestate = False
        if gameObj.winCheck() == 3:
            print('Its a draw!!!')
            gameObj.gamestate = False
    except:
        print 'Invalid input please enter a valid  number'
        gameObj.printBoard()