from src.board import Board
from src.player import Player


class Move:
    """Given a board, player, and index attempt to place the player's piece on
    the Square at that index"""

    def __init__(self, board: Board, player: Player, index: int):
        self.board = board
        self.piece = player.piece

    def check_square(self, index: int):
        """Check if square already has a piece"""
        pass
