from __future__ import print_function
from move import *
from block import *
class board:
    w = 1
    h = 1
    matrix = [[0 for x in range(w)] for x in range(h)]
    flatList = [item for sublist in matrix for item in sublist]

    def show(self, matrix):
        print(self.w,',',self.h,',',sep='')
        for x in xrange(0, self.h):
            row = ''
            for y in xrange(0, self.w):
                row += str(self.matrix[x][y])
                row +=','
            print(row,sep='')

    def clone(self, matrix):
        newObj = self
        return newObj

    def isSolved(self, matrix):
        solved = True
        for x in xrange(0, self.h):
            for y in xrange(0, self.w):
                if self.matrix[x][y] == -1:
                    solved = False
        return solved

    def getBlocks(self, matrix):
        blocks = list(set(self.flatList) - set([-1, 0, 1]))
        return blocks

    def moves(self,matrix,blocks):
        moves = []
        currblocks = []
        for b in blocks:
            for x in xrange(0, self.h):
                for y in xrange(0, self.w):
                    if self.matrix[x][y] == b:
                        #print('position of',b,'is: ',x,',',y)
                        for obj in currblocks:
                            if obj.id == b:
                                for pos in obj.position:
                                    if pos[0] != x:
                                        obj.height += 1
                                    if pos[1] != y:
                                        obj.width += 1
                                obj.position.append((x,y))
                                break
                        else:
                            newBlock = block()
                            newBlock.id = b
                            newBlock.height = 1
                            newBlock.width = 1
                            newBlock.position = []
                            newBlock.position.append((x,y))
                            currblocks.append(newBlock)
        for obj in currblocks:
            #print(obj.id,',',obj.height,',',obj.width,',',obj.position)
            moveUp = True
            moveRight = True
            moveDown = True
            moveLeft = True
            for pos in obj.position:
                if self.matrix[pos[0]-1][pos[1]] != 0 and self.matrix[pos[0]-1][pos[1]] != obj.id:
                    moveUp = False
                if self.matrix[pos[0]][pos[1]+1] != 0 and self.matrix[pos[0]][pos[1]+1] != obj.id:
                    moveRight = False
                if self.matrix[pos[0]+1][pos[1]] != 0 and self.matrix[pos[0]+1][pos[1]] != obj.id:
                    moveDown = False
                if self.matrix[pos[0]][pos[1]-1] != 0 and self.matrix[pos[0]][pos[1]-1] != obj.id:
                    moveLeft = False
            if moveUp:
                newMove = move()
                newMove.block = obj.id
                newMove.direction = 0
                moves.append(newMove)
            if moveRight:
                newMove = move()
                newMove.block = obj.id
                newMove.direction = 1
                moves.append(newMove)
            if moveDown:
                newMove = move()
                newMove.block = obj.id
                newMove.direction = 2
                moves.append(newMove)
            if moveLeft:
                newMove = move()
                newMove.block = obj.id
                newMove.direction = 3
                moves.append(newMove)

        for obj in moves:
            print('blockid:',obj.block,',direction:',obj.direction)
