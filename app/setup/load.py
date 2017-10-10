from board import *
fname = raw_input('Please provide a file and absolute path.. and then hit RETURN / ENTER \n')

with open(fname) as f:
    content = f.read()

boardObj = board()
inputNums = content.replace("\n", "").split(",")
boardObj.w = int(inputNums[0])
boardObj.h = int(inputNums[1])
inputNumsIndex = int(2)
for x in xrange(0, boardObj.h):
    for y in xrange(0, boardObj.w):
        print x , y
        #print int(inputNums[inputNumsIndex])
        boardObj.matrix[x][y] = int(inputNums[inputNumsIndex])
        inputNumsIndex += 1

print boardObj.matrix
