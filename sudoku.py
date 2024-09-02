import numpy as np

# sudoku = np.zeros((9,9))
def returnZero(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                return (i,j)

def isvalid(sudoku,pos,nums):
    for i in range(9):
        if sudoku[i][pos[1]] == nums and (i,pos[1])!=pos:
            return False
        if sudoku[pos[0]][i] == nums and (pos[0],i)!=pos:
            return False
    a = pos[0]//3
    a*=3
    b = pos[1]//3
    b*=3
    for i in range(3):
        for j in range(3):
            if sudoku[a+i][b+j] == nums and (a+i,b+j)!=pos:
                return False
    return True


def sudokusolve(sudoku):
    position = returnZero(sudoku)
    if not position:
        return True
    for nums in range(9):
        if isvalid(sudoku,position,nums+1):
            sudoku[position[0]][position[1]] = nums+1
            if sudokusolve(sudoku):
                return True
            sudoku[position[0]][position[1]] = 0
    return False
if __name__=="__main__":
    sudoku = np.array(
        [
            [0,0,4,7,0,0,0,0,6],
            [5,0,0,6,0,0,0,7,2],
            [0,0,0,0,0,0,8,0,0],
            [0,0,2,0,0,6,5,3,0],
            [0,4,0,2,0,9,0,6,0],
            [0,8,1,3,0,0,2,0,0],
            [0,0,3,0,0,0,0,0,0],
            [8,5,0,0,0,1,0,0,3],
            [4,0,0,0,0,8,7,0,0]
        ]
    )
    sudokusolve(sudoku)
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j],end=" ")
        print()
