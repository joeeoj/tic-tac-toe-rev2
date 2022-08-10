from typing import Optional

from src.exceptions import PieceAlreadySetError
from src.piece import Piece


class Square:
    def __init__(self, index: int, coords: tuple[int], piece: Optional[Piece] = None):
        self._index = index
        self._coords = coords
        self._piece = piece
        self._row, self._col = coords

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, piece):
        """Can only set once if the piece is None, otherwise raise an error"""
        if self._piece is not None:
            raise PieceAlreadySetError(f"Square already set with piece '{str(self._piece)}'.")
        else:
            self._piece = piece
