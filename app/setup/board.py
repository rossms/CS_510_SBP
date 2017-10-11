from __future__ import print_function
class board:
    w = 1
    h = 1
    matrix = [[0 for x in range(w)] for x in range(h)]

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
