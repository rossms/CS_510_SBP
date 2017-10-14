import setup.load as loader
from setup.move import *
#load a board from disk
currentBoard = loader.loadBoard()
#print out the current board
#currentBoard.show(currentBoard)
#clone currentboard into a new object newBoard
newBoard = currentBoard.clone(currentBoard)
#check if the puzzle is solved
#print(currentBoard.isSolved(currentBoard))
#get all blocks in the current state
#currentBlocks = currentBoard.getBlocks(currentBoard)
#get moves for currentboard and block(s)
#currentBoard.moves(currentBoard, [2])
#gamePlay = currentBoard.moves(currentBoard, currentBlocks)
#move
newMove = move()
newMove.block = 2
newMove.direction = 3
#newBoard = newMove.applyMove(currentBoard,newMove,gamePlay.blocks)
#newBoard = newMove.applyMoveCloning(currentBoard,newMove,gamePlay.blocks)
#compare two boards to see if they are identical
#print(newBoard.simpleComparison(newBoard,testBoard))
#normalize board and then compare
#normalizedBoard = newBoard.normalize(newBoard)
#print(newBoard.simpleComparison(normalizedBoard,normalizedBoard))
#random walks - 1 get all moves, apply move at random, normalize, check goal,
#repeat until goal or N (number of random moves to try)
currentBoard.randomWalks(currentBoard, 5)
