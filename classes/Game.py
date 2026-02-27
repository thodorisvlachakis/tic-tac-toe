from classes.Grid import *
from classes.Player import Player
from classes.RandomPlayer import RandomPlayer
from classes.StrategyPlayer import StrategyPlayer

class Game:
    def __init__(self, player1_name, player2_name):
        self._grid = Grid()
        self._player1 = Player(player1_name, 'X')
        self._player2 = Player(player2_name, 'O')

    def get_player(self, player_name):
        if (player_name != self._player1.get_name()):
            return self._player2
        
        return self._player1
    
    def get_players(self):
        return [self._player1, self._player2]

    def get_grid(self):
        return self._grid

    def modify_player_name(self, player_name: str, new_name: str):
        if (player_name == self._player1.get_name()):
            self._player1.set_name(new_name)
        else:
            self._player2.set_name(new_name)

    def modify_player_type(self, player_name: str, player_type: str):
        if (player_name == self._player1.get_name()):
            if (player_type == 'Random Player'):
                self._player1 = RandomPlayer(player_name, self._player1.get_symbol())
            elif (player_type == 'Strategy Player'):
                self._player1 = StrategyPlayer(player_name, self._player1.get_symbol())
        else:    
            if (player_type == 'Random Player'):
                self._player2 = RandomPlayer(player_name, self._player2.get_symbol())
            elif (player_type == 'Strategy Player'):
                self._player2 = StrategyPlayer(player_name, self._player2.get_symbol())
    
    def select_game_mode(self):
        n_players = 2
        computer_player_type = None
        
        print('Select game mode :')
        print('1. Play 1 vs 1')
        print('2. Play against computer')

        valid_choice = False
        while(valid_choice !=True):
            choice = input('Make your choice : ')
            if(choice == '1' or choice == '2'):
                valid_choice = True
            else:
                print('Invalid choice.')

        # If "play against computer" is choosen
        if (choice == '2'):
            print("\n Choose opponent's level :")
            print('1. Easy')
            print('2. Advanced')
            
            n_players = 1
            valid_choice = False
            while(valid_choice !=True):
                choice = input('Make your choice : ')
                if(choice == '1' or choice == '2'):
                    valid_choice = True
                else:
                    print('Invalid choice.')
            
            if (choice != '2'):
                computer_player_type = 'Random Player'
            else:
                computer_player_type = 'Strategy Player'
        
        return n_players, computer_player_type

    def clear_grid(self):
        self._grid = Grid()

    def is_over(self):
        game_over = False
        winner = None

        # 1. Check for a winner
        for i in range(3):
            
            # Row equal elements

            if (self._grid.get_grid_array()[i, 0] != ' ' and 
                np.all(self._grid.get_grid_array()[i, :] == self._grid.get_grid_array()[i, 0])):
                game_over = True
                winner = self._player1
                if (self._player1.get_symbol() != self._grid.get_grid_array()[i, 0]):
                    winner = self._player2
                break

            # Column equal elements

            elif (self._grid.get_grid_array()[0, i] != ' ' and 
                  np.all(self._grid.get_grid_array()[:, i] == self._grid.get_grid_array()[0, i])):
                game_over = True
                winner = self._player1
                if (self._player1.get_symbol() != self._grid.get_grid_array()[0, i]):
                    winner = self._player2
                break

        # Diagonal equal elements

        if (self._grid.get_grid_array()[0, 0] != ' ' and 
            np.all(np.diag(self._grid.get_grid_array()) == self._grid.get_grid_array()[0, 0])):
            game_over = True
            winner = self._player1
            if (self._player1.get_symbol() != self._grid.get_grid_array()[0, 0]):
                winner = self._player2

            return game_over, winner
        
        elif (self._grid.get_grid_array()[2, 0] != ' ' and 
              np.all(np.diag(np.flipud(self._grid.get_grid_array())) == self._grid.get_grid_array()[2, 0])):
            game_over = True
            winner = self._player1
            if (self._player1.get_symbol() != self._grid.get_grid_array()[2, 0]):
                winner = self._player2

            return game_over, winner
        
        # 2. Check for tie given that there is no winner.
        if (np.all(self._grid.get_grid_array() != ' ')):
            game_over = True

        return game_over, winner
    
    def run_game_loop(self, player_1: Player, player_2: Player):
        game_over = False
        winner = None

        self._grid.display_grid()

        while(game_over != True):

            print("It's " + player_1.get_name() + "'s turn.")
            player_1.make_move(self._grid)
            self._grid.display_grid()
            game_over, winner = self.is_over()
            if (game_over == True):
                break

            print("It's " + player_2.get_name() + "'s turn.")
            player_2.make_move(self._grid)
            self._grid.display_grid()
            game_over, winner = self.is_over()

        return winner
