from Grid import *

class Player:
    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol
        self._is_computer = False
        self._player_type = None # It's used only for computer

    # Setters and getters
    def set_name(self, new_name: str):
        self._name = new_name
    
    def set_symbol(self, new_symbol: str):
        self._symbol = new_symbol

    def set_player_type(self, new_player_type: str):
        self._player_type = new_player_type

    def play_as_computer(self, player_type: str):
        self._is_computer = True
        self._name = 'Computer'
        self.set_player_type(player_type)

    def get_name(self):
        return self._name
    
    def get_symbol(self):
        return self._symbol
    
    def get_is_computer(self):
        return self._is_computer
    
    def get_player_type(self):
        return self._player_type
    
    # Making move

    def make_move(self, current_grid: Grid):
        if (self._is_computer != True):
            # Act like a human playing the game
            
            valid_update = False
            while (valid_update != True):
                choosen_position = eval(input('Choose the position on the board for your move. Use the format' \
                ' "row_choice", "column_choice": '))

                if(type(choosen_position) == tuple and len(choosen_position) == 2
                    and type(choosen_position[0]) == int and type(choosen_position[1]) == int):

                    grid_actual_position = choosen_position[0] - 1 , choosen_position[1] - 1

                    valid_update = current_grid.update_grid(grid_actual_position, self._symbol)

                else:
                    print('Invalid choosen position format.')

        else:
            # Act like a computer playing the game
            print('This player is a computer. A different version of make_move() function must be called.')
