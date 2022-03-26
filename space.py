import numpy as np
from block import Block

import typing

class Space:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.blocks = []
        self.space = np.array([["000" for _ in range(col)] for _ in range(row)], dtype=object)


    def add_block(self, block):
        col = block.col
        block.row = self.row_availability(col)
        if block in self.blocks:
            raise Exception("Same object can't be in two places at once")
        else:
            self.blocks.append(block)
        self.update_space()


    def refresh_space(self):
        self.space = np.array([["000" for _ in range(self.col)] for _ in range(self.row)], dtype=object)


    def update_space(self):
        self.refresh_space()
        for block in self.blocks:
            self.space[block.row][block.col] = block.name


    def add_blocks(self, blocks):
        for block in blocks:
            self.add_block(block)


    def row_availability(self,col):
        if col > self.col:
            raise IndexError('Out of column')
        else:
            if self.space[0][col] != '000':
                raise Exception("Couldn't place the block in the given column,Out of space")
            else:
                for i in range(1,self.row):
                    if self.space[i][col] != '000':
                        return i-1
        return self.row-1


    def move_block(self,block, new_col):
        now_row = block.row
        if self.space[now_row-1][block.col] != '000':
            raise Exception("can't move the block another block is in the way")
        else:
            block.col = new_col
            block.row = self.row_availability(block.col)
            self.update_space()


if __name__ == "__main__":
    k = Space(5, 4)
    block1 = Block("B01", 0, k)
    block2 = Block("B02", 0, k)
    block3 = Block("B03", 0, k)
    block4 = Block("A01", 1, k)
    blocks = [block1, block2, block3, block4]
    print(k.space)
    k.add_blocks(blocks)
    print(k.space)
    k.move_block(block3, 1)
    print(k.space)
    # k.move_block(block1, 2)