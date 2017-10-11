import setup.load as loader

#load a board from disk
currentBoard = loader.loadBoard()
#print out the current board
currentBoard.show(currentBoard)
#clone currentboard into a new object newBoard
newBoard = currentBoard.clone(currentBoard)
#check if the puzzle is solved
print(currentBoard.isSolved(currentBoard))
#get all blocks in the current state
print(currentBoard.getBlocks(currentBoard))
#get moves for currentboard and block(s)
currentBoard.moves(currentBoard, [2])
