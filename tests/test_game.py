import datetime

import pytest

from src.board import Board
from src.exceptions import InvalidNumPlayers
from src.game import Game
from src.player import Player


def test_init_game_with_board():
    players = [Player("Joe"), Player("Jim")]
    game = Game(players)
    assert isinstance(game.board, Board)


def test_correct_num_players():
    players = [Player("Joe"), Player("Bob")]
    game = Game(players)
    assert len(players) == len(game.players)


def test_below_min_players():
    players = [Player("Bob")]
    with pytest.raises(InvalidNumPlayers):
        game = Game(players)


def test_above_max_players():
    players = [Player("Joe"), Player("Jim"), Player("Bob")]
    with pytest.raises(InvalidNumPlayers):
        game = Game(players)


def test_game_start_time_is_now():
    players = [Player("Joe"), Player("Jim")]
    now = datetime.datetime.now()
    game = Game(players)

    fmt = "%Y-%m-%d %H:%M"
    assert now.strftime(fmt) == game.start_datetime.strftime(fmt)


def test_player_one_first_turn():
    players = [Player("Joe"), Player("Jim")]
    now = datetime.datetime.now()
    game = Game(players)

    assert game.turn == players[0]
