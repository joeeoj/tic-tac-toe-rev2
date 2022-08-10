from src.board import Board


def test_board_pieces_empty_on_init():
    board = Board()
    assert all([s.piece is None for s in board.state])
