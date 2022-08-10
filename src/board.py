from curses.ascii import EM
from itertools import groupby
from urllib.parse import non_hierarchical

from more_itertools import chunked

from src.square import Square


ROW_LEN, COL_LEN = 3, 3

EMPTY_STATE = []
index = 1
for x in range(ROW_LEN):
    for y in range(COL_LEN):
        EMPTY_STATE.append(Square(index, (x, y)))
        index += 1


def all_equal(iterable):
    """Returns True if all the elements are equal to each other
    https://docs.python.org/3/library/itertools.html#itertools-recipes"""
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def all_pieces_equal(squares: list[Square]) -> bool:
    nonempty_pieces = [s.piece for s in squares]
    return len(squares) == len(nonempty_pieces) and all_equal(nonempty_pieces)


class Board:
    """
    3x3 board
    ---------
    [1,2,3]
    [4,5,6]
    [7,8,9]
    """

    def __init__(self, state: list[Square] = EMPTY_STATE):
        self.state = state

    def _row_winner(self) -> bool:
        """
        [1,2,3]
        [4,5,6]
        [7,8,9]
        """
        for row in chunked(self.state, ROW_LEN):
            if all_pieces_equal(row):
                return True
        return False

    def _col_winner(self) -> bool:
        """
        [1,4,7]
        [2,5,8]
        [3,6,9]
        """
        stop = (ROW_LEN * COL_LEN) + 1
        for i in range(1, ROW_LEN + 1):
            if all_pieces_equal(self.state[i:stop:ROW_LEN]):
                return True
        return False

    # TODO (all of it)
    def _diag_winner(self) -> bool:
        """
        [1,5,9]
        [3,5,7]
        """
        pass
