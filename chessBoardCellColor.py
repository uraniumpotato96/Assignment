"""Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.
"""


def findColor(cell):
    if (cell[0] in 'ACEG' and int(cell[1]) % 2 != 0):
        return 'Black'
    if (cell[0] in 'BDFH' and int(cell[1]) % 2 == 0):
        return 'Black'
    else:
        return 'White'

def chessBoardCellColor(cell1,cell2):
    return findColor(cell1) == findColor(cell2)

print chessBoardCellColor('A1','B2')







