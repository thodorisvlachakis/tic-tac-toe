import numpy as np

class Grid:
    def __init__(self):
        self._current_grid = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def set_grid_array(self, new_grid_array: np.ndarray):
        self._current_grid = new_grid_array.copy()

    def get_grid_array(self):
        return self._current_grid
    
    def copy(self):
        grid_copy = Grid()
        grid_copy.set_grid_array(self._current_grid)

        return grid_copy
    
    def update_grid(self, choosen_position: tuple, player_symbol):
        row, col = choosen_position

        if (row < 0 or row > 2 or col < 0 or col > 2):
            print('Invalid choosen position. Out of bounds.')
            return False 
        
        if (self._current_grid[choosen_position] != ' '):
            print('Invalid choosen position. Already reserved.')
            return False
        self._current_grid[choosen_position] = player_symbol
        return True
    
    def is_full(self):
        if (' ' not in self._grid):
            return True
        
        return False
    
    def is_empty(self):
        return np.all(self._current_grid == ' ')
    
    def display_grid(self):
        #print("  |  |  ")
        for i in range(3):
            for j in range(3):
                if (j != 2):
                    print(" " + str(self._current_grid[i][j]) + " |", end="")
                else:
                    print(" " + str(self._current_grid[i][j]) + " ")
            
            if (i !=2):
                print("------------")
        
        #print("  |  |  ")
