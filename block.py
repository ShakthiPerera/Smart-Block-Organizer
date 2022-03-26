import numpy as np

class Block:
    def __init__(self, name, col_pos, space):
        self.name = name
        self.col = col_pos
        self.row = None
        self.space = space
