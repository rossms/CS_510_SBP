from __future__ import print_function
from move import *
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
        for b in blocks:
            for x in xrange(0, self.h):
                for y in xrange(0, self.w):
                    if self.matrix[x][y] == b:
                        print('position of',b,'is: ',x,',',y)
                        if self.matrix[x][y-1] == 0:
                            newMove = move()
                            newMove.block = b
                            newMove.direction = 3
                            print(newMove)
                            moves.append(newMove)
        for obj in moves:
            print(obj.block,',',obj.direction)
