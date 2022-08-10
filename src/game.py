"""Game is a combination of a board and a list of players"""
import datetime
import itertools

from src.board import Board
from src.exceptions import InvalidNumPlayers
from src.move import Move
from src.player import Player


MIN_PLAYERS, MAX_PLAYERS = 2, 2


class Game:
    def __init__(self, players: list[Player]):
        self.board = Board()

        if len(players) > MAX_PLAYERS or len(players) < MIN_PLAYERS:
            raise InvalidNumPlayers(
                f"Invalid number of players '{len(players)}' -- Min of {MIN_PLAYERS} and max of {MAX_PLAYERS} players allowed"
            )
        else:
            self.players = players

        self.start_datetime = datetime.datetime.now()
        self.stop_datetime = None

        # defaults to first player and keeps cycling through
        self._turn = itertools.cycle(self.players)

    @property
    def turn(self):
        return next(self._turn)

    def check_winner(self):
        pass
