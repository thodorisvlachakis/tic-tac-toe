from Player import *

class StrategyPlayer(Player):
    # This class refers only to a "computer" player.
    # Strategy Player is a type of player who acts smartly in each
    # round considering what is the current state of the grid and
    # which are the possible actions that could put him in an
    # advantageous position.
    
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
        self.play_as_computer('Strategy Player')
        self._first_round = True
        self._favorite_positions = [(0,0), (0,2), (2,0), (2,2)]
        self._opponent_symbol = None

    def set_opponent_symbol(self):
        self._opponent_symbol = 'X'
        if (self._symbol != 'O'):
            self._opponent_symbol = 'O'

    def get_opponent_symbol(self):
        return self._opponent_symbol
    
    def get_favorite_positions(self):
        return self._favorite_positions

    def reset_properties(self):
        self._first_round = True
        self._favorite_positions = [(0,0), (0,2), (2,0), (2,2)]
        self._opponent_symbol = None

    def possible_triplet(self, current_grid: Grid, symbol: str):
        possible_triplet = False
        possible_triplet_positions = [] # It stores the positions must be choosen to make a triplet on the grid.

        for i in range(3):

            # Possible triplets in rows

            values, indices, counts = np.unique(current_grid.get_grid_array()[i, :], return_index=True, return_counts=True)

            if (len(counts) == 2 and ' ' in values and values[np.where(counts == 2)[0]] == symbol):
                possible_triplet = True
                possible_triplet_positions.append( (i, indices[np.where(counts == 1)[0]][0]) )

            # Possible triplets in columns

            values, indices, counts = np.unique(current_grid.get_grid_array()[:, i], return_index=True, return_counts=True)
            
            if (len(counts) == 2 and ' ' in values and values[np.where(counts == 2)[0]] == symbol):
                possible_triplet = True
                possible_triplet_positions.append( (indices[np.where(counts == 1)[0]][0], i) )

        # Possible triplets in diagonals
        
        # Left-to-Right diagonal
        values, indices, counts = np.unique(np.diag(current_grid.get_grid_array()), return_index=True, return_counts=True)

        if (len(counts) == 2 and ' ' in values and values[np.where(counts == 2)[0]] == symbol):
            possible_triplet = True
            possible_triplet_positions.append( (indices[np.where(counts == 1)[0]][0],
                                                indices[np.where(counts == 1)[0]][0]))
            
        # Right-to-Left diagonal
        values, indices, counts = np.unique(np.diag(np.flipud(current_grid.get_grid_array())), return_index=True, return_counts=True)

        if (len(counts) == 2 and ' ' in values and values[np.where(counts == 2)[0]] == symbol):
            possible_triplet = True
            possible_triplet_positions.append( (2 - indices[np.where(counts == 1)[0]][0],
                                                indices[np.where(counts == 1)[0]][0]))
            

        return possible_triplet, possible_triplet_positions
    
    def search_grid_available_positions(self, current_grid: Grid):
        # This function implements the searching for available positions on the current grid
        # and then updates the self._favorite_positions list putting in only these positions.
        # The way with which the "Strategy Player" searches on the grid for available 
        # positions is part of their "smart choice strategy".
        
        self._favorite_positions = []

        # First search the four corners of the grid
        for position in [(0,0), (0,2), (2,0), (2,2)]:
            if (current_grid.get_grid_array()[position] == ' '):
                self._favorite_positions.append(position)

        # Secondly search the cross in the middle of the grid
        self._favorite_positions.extend((row, 1) 
                                        for row in np.where(current_grid.get_grid_array()[:, 1] == ' ')[0])
        
        self._favorite_positions.extend((1, column) 
                                        for column in np.where(current_grid.get_grid_array()[1, :] == ' ')[0])
        
        # Remove duplicate (1,1) if it exists in _favorite_positions
        if ((1,1) in self._favorite_positions):
            self._favorite_positions.pop(np.where(np.array(self._favorite_positions) == (1,1))[0][1])

    def is_good_build_up(self, current_grid: Grid, choosen_position: tuple):
        current_grid_copy = current_grid.copy()
        
        possible_triplet = False
        strong_move = False
        
        if(current_grid_copy.get_grid_array()[choosen_position] == ' '):

            current_grid_copy.get_grid_array()[choosen_position] = self._symbol

            possible_triplet, possible_triplet_positions = self.possible_triplet(current_grid_copy, self._symbol)
            
            # print('Here is the length')
            # print(len(possible_triplet_positions))
            # print(possible_triplet_positions)

            if (len(possible_triplet_positions) > 1):
                strong_move = True
        
        return possible_triplet, strong_move

    def make_move(self, current_grid: Grid):
        # Act like a computer playing the game.
        # This version of make_move refers to the "Strategy Player" player type,
        # so it implements the "smart choice strategy" of this player type.
        
        # Reset the properties of "Strategy Player" in case it's not the first game
        if(current_grid.is_empty() == True or (' ' in np.unique(current_grid.get_grid_array()) and 
                                               len(np.unique(current_grid.get_grid_array())) == 2)):
           self.reset_properties()

        if (self._first_round != False):
            self.set_opponent_symbol()
            
            if(current_grid.is_empty() != True 
               and np.any([current_grid.get_grid_array()[position] == self._opponent_symbol
               for position in self._favorite_positions])):
                
                # "Strategy Player" plays second and the opponent has choosen a corner. So, play defensivly.
                current_grid.update_grid((1,1), self._symbol)
            #     print('Executed')
            #     print(self._favorite_positions)
            #     print(self._opponent_symbol)
            #     print("Look "+ str([current_grid.get_grid_array()[position] == self._opponent_symbol
            #    for position in self._favorite_positions]))
            #     print(current_grid.is_empty())

            else:
                # "Strategy Player" plays either first or second but the oppenent hasn't choosen a corner.
                # So, play attacking.
                choosen_position = self._favorite_positions[np.random.randint(4)]
                current_grid.update_grid(choosen_position, self._symbol)
                # print(choosen_position)
                # print(self._favorite_positions)

            self._first_round = False

        else:
            # First, check if there is any chance of winning immediately.
            # Secondly, check for a possible danger.

            for symbol in [self._symbol, self._opponent_symbol]:
                possible_triplet_exists, possible_triplet_positions = self.possible_triplet(current_grid, symbol)

                if (possible_triplet_exists):
                    choosen_position = possible_triplet_positions[np.random.randint(len(possible_triplet_positions))]
                    current_grid.update_grid(choosen_position, self._symbol)
                    # print('Executed 2')
                    # print(self._favorite_positions)
                    return
                
            self.search_grid_available_positions(current_grid)

            # Thirdly (there are no possible triplets on the grid), check for moves that can bring 
            # the victory in two time steps forward.
            
            choosen_position_alternatives = []
            
            for position in self._favorite_positions:
                possible_triplet_exists, strong_move = self.is_good_build_up(current_grid, position)
                # print(possible_triplet_exists)
                if(possible_triplet_exists != False):
                    choosen_position_alternatives.append(position)
                    
                    if (strong_move != False):
                        choosen_position = choosen_position_alternatives[len(choosen_position_alternatives) - 1]
                        current_grid.update_grid(choosen_position, self._symbol)
                        # print('Executed 3')
                        # print(self._favorite_positions)
                        return
                
                if(len(choosen_position_alternatives) > 0 and 
                   position == self._favorite_positions[len(self._favorite_positions) - 1]):
                    for pos in list(set([(0,0), (0,2), (2,0), (2,2)]) & set(choosen_position_alternatives)):
                        
                        if(np.any(current_grid.get_grid_array()[pos[0], :] == self._symbol) or
                           np.any(current_grid.get_grid_array()[:, pos[1]] == self._symbol)):
                            choosen_position = pos
                        
                            current_grid.update_grid(choosen_position, self._symbol)
                            # print('Executed 3.1')
                            # print(self._favorite_positions)
                            return

            # Otherwise, choose a position to play from the remaining possible ones.

            choosen_position = self._favorite_positions[np.random.randint(len(self._favorite_positions))]
            current_grid.update_grid(choosen_position, self._symbol)
            # print('Executed 4')
            # print(self._favorite_positions)
