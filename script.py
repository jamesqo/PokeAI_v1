from game_state import GameState
from move_selector import MoveSelector
from player import Player

sel = MoveSelector()
# train it...
game_state = GameState(
    us=Player(
        mon_0=Pokemon(
            )),
    them=Player(
        ))
next_move = sel.predict(game_state)
next_game_state = game_state.execute(next_move)
