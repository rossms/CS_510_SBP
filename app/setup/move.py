class move():
    block = 0
    direction = 0 #0 = up, 1 = right, 2 = down, 3 = left

    def applyMove(self, board, move, blocks):
        for b in blocks:
            if b.id == move.block:
                for pos in b.position:
                    if move.direction == 0:
                        board.matrix[pos[0]][pos[1]] = 0
                        board.matrix[pos[0]-1][pos[1]] = b.id
                    elif move.direction == 1:
                        board.matrix[pos[0]][pos[1]] = 0
                        board.matrix[pos[0]][pos[1]+1] = b.id
                    elif move.direction == 2:
                        board.matrix[pos[0]][pos[1]] = 0
                        board.matrix[pos[0]+1][pos[1]] = b.id
                    elif move.direction == 3:
                        board.matrix[pos[0]][pos[1]] = 0
                        board.matrix[pos[0]][pos[1]-1] = b.id
        return board
