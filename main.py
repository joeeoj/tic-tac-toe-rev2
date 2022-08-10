from src.game import Game
from src.move import Move
from src.player import Player


player_one = Player("Mike")
player_two = Player("Joe")

game = Game([player_one, player_two])


m1 = Move(game, player_one, 1)
game.board = m1.


# just take a square index as the input
# assumes player 1 starts first
game.move(1)

# player 2
game.move(2)
