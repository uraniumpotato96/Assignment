class GameTicTacToe:
    def __init__(self):
        self.positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.chance = True
        self.gamestate = True
        self.player1 = 'X'
        self.player2 = 'O'
        self.previousInputs = []

    def printBoard(self):
        print ('------------')
        print ('|{0}|{1}|{2}|\n'.format(self.positions[0], self.positions[1], self.positions[2]))
        print ('|{0}|{1}|{2}|\n'.format(self.positions[3], self.positions[4], self.positions[5]))
        print ('|{0}|{1}|{2}|\n'.format(self.positions[6], self.positions[7], self.positions[8]))
        print('-------------')

    def updateBoard(self,a,choice):
        if a not in self.previousInputs and a in range(1, 10):
            self.previousInputs.append(a)
            if choice:
                self.positions[a - 1] = self.player1
                return self.positions
            else:
                self.positions[a - 1] = self.player2
                return self.positions
        else:
            print 'please select a valid position.'
            return 2

    def winCheck(self):
        if self.positions[0] == self.positions[1] == self.positions[2] == self.player1 or self.positions[3] == self.positions[4] == self.positions[5] == self.player1 or self.positions[6] == self.positions[7] == self.positions[8] == self.player1 or self.positions[0] == self.positions[3] == self.positions[6] == self.player1 or self.positions[1] == self.positions[4] == self.positions[7] == self.player1 or self.positions[2] == self.positions[5] == self.positions[8] == self.player1 or self.positions[0] == self.positions[4] == self.positions[8] == self.player1 or self.positions[2] == self.positions[4] == self.positions[6] == self.player1:
            return 1
        if self.positions[0] == self.positions[1] == self.positions[2] == self.player2 or self.positions[3] ==self.positions[4] == self.positions[5] == self.player2 or self.positions[6] == self.positions[7] ==self.positions[8] == self.player2 or self.positions[0] == self.positions[3] == self.positions[6] == self.player2 or self.positions[1] == self.positions[4] == self.positions[7] == self.player2 or self.positions[2] == self.positions[5] == self.positions[8] == self.player2 or self.positions[0] == self.positions[4] == self.positions[8] == self.player2 or self.positions[2] == self.positions[4] == self.positions[6] == self.player2:
            return 2
        if len(self.previousInputs) == 9:
            return 3

