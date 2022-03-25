import numpy as np
from block import Block

import typing

class Space:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.space = np.array([["000" for _ in range(col)] for _ in range(row)], dtype=object)

    def add_block(self, block):
        row, col = block.x, block.y
        self.space[row][col] = block.name

    def row_availability(self,col):
        if col > self.col:
            raise IndexError('Out of column')
        else:
            for i in range(self.row):
                if self.space[i] != '000':
                    return i-1





if __name__ == "__main__":
    block1 = Block("B01", (4, 0))
    k = Space(5,4)
    print(k.space)
    k.add_block(block1)
    print(block1.name)
    print(k.space)