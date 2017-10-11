from board import *

def loadBoard():
    fname = raw_input('Please provide a file and absolute path.. and then hit RETURN / ENTER \n')

    with open(fname) as f:
        content = f.read()
    boardObj = board()
    inputNums = content.replace("\n", "").split(",")
    boardObj.w = int(inputNums[0])
    boardObj.h = int(inputNums[1])
    boardObj.matrix = [[0 for x in range(boardObj.w)] for x in range(boardObj.h)]
    inputNumsIndex = int(2)
    for x in xrange(0, boardObj.h):
        for y in xrange(0, boardObj.w):
            boardObj.matrix[x][y] = int(inputNums[inputNumsIndex])
            inputNumsIndex += 1
    boardObj.flatList = [item for sublist in boardObj.matrix for item in sublist]
    return boardObj
