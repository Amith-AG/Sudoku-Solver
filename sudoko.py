from pprint import pprint
def nextEmpty_space(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    return None,None
def isValidGuess(puzzle,guess,row,col):
    # row check
    row_list=puzzle[row]
    if guess in row_list:
        return False
    # col check
    col_list=[puzzle[i][col] for i in range(9)]
    if guess in col_list:
        return False
    # 3x3 square check
    row_start=(row//3)*3
    col_start=(col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    return True
def sudokuSolver(puzzle):
    row,col=nextEmpty_space(puzzle)
    if row==None:
        return True
    for guess in range(1,10):
        if isValidGuess(puzzle,guess,row,col):
            puzzle[row][col]=guess
            if sudokuSolver(puzzle):
                 return True
        puzzle[row][col]=-1
    return False
if __name__=="__main__":
    puzzle=[
       [-1,4,-1, 9,-1,-1, -1,-1,-1],
       [-1,-1,-1,-1,-1,3,-1,4,8],
       [6,-1,8, -1,-1,-1, 3,7,-1],
       [9,-1,4, 3,-1,-1, -1,-1,1],
       [5,8,-1, 1,-1,6, -1,-1,-1],
       [-1,-1,-1,-1,-1,8,7,-1,-1],
       [-1,-1,-1,-1,5,9,6,-1,-1],
       [8,3,-1, -1,4,2, 9,1,7],
       [2,6,9,-1,3,1, -1,8,5]
    ]
print(sudokuSolver(puzzle))        
pprint(puzzle)


