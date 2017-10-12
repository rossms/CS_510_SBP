import setup.load as loader
from setup.move import *
#load a board from disk
currentBoard = loader.loadBoard()
#print out the current board
currentBoard.show(currentBoard)
#clone currentboard into a new object newBoard
newBoard = currentBoard.clone(currentBoard)
#check if the puzzle is solved
#print(currentBoard.isSolved(currentBoard))
#get all blocks in the current state
currentBlocks = currentBoard.getBlocks(currentBoard)
#get moves for currentboard and block(s)
#currentBoard.moves(currentBoard, [2])
gamePlay = currentBoard.moves(currentBoard, currentBlocks)
#move
newMove = move()
newMove.block = 2
newMove.direction = 3
newBoard = newMove.applyMove(currentBoard,newMove,gamePlay.blocks)
currentBoard.show(newBoard)
