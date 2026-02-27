from classes.Player import *

class RandomPlayer(Player):
    # This class refers only to a "computer" player.
    # Random Player is a type of player who, in each round, randomly selects
    # a position on the grid from the available ones to place his symbol.

    def __init__(self, name, symbol):
        super().__init__(name, symbol)
        self.play_as_computer('Random Player')

    def make_move(self, current_grid: Grid):
        # Act like a computer playing the game.
        # This version of make_move refers to the "Random Player" player type,
        # so it implements the "random choice strategy" of this player type.
        
        available_positions = np.where(current_grid.get_grid_array() == ' ') # The result is a tuple
        
        # Select a position for the move, randomly
        random_position_idx = np.random.randint(len(available_positions[0]))
        choosen_position = available_positions[0][random_position_idx], available_positions[1][random_position_idx]
        
        current_grid.update_grid(choosen_position, self._symbol)
