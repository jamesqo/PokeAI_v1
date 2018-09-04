class MoveSelector(object):
    def __init__(self):
        pass

    def fit(self):
        pass

    def predict(self, game_state):
        possible_moves = game_state.possible_moves
        return max(possible_moves, key=lambda move: reward_of(move, game_state))
