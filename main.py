from classes.Game import *

def toss_a_coin():
    if (np.random.rand() < 0.5):
        return True
    return False

def play_game():
    print('\nWelcome to Tic Tac Toe ! \n')
    
    game = Game('p1', 'p2')
    change_game_mode = True
    while (change_game_mode != False):
        n_players, computer_player_type = game.select_game_mode()
        winner = None

        if(n_players != 1):
            player1_name = input("Select a name for player 1 (symbol 'X') : ")

            player2_name = input("Select a name for player 2 (symbol 'O') : ")

            game.modify_player_name('p1', player1_name)
            game.modify_player_name('p2', player2_name)

        else:
            player1_name = input("Select your name (your symbol is 'X') : ")
            game.modify_player_name('p1', player1_name)
            game.modify_player_type('p2', computer_player_type)

        play_again = True
        while (play_again != False):

            # Toss a coin in order to decide game order
            if (toss_a_coin() != False):
                winner = game.run_game_loop(game.get_players()[0], game.get_players()[1])
            else:
                winner = game.run_game_loop(game.get_players()[1], game.get_players()[0])

            if (winner != None):
                print('The winner is ' + winner.get_name() + ' !')
            else:
                print("It's a tie !")
            
            print('\nDo you want to play again ? Choose below :')
            print('1. Play again')
            print('2. Select game mode')
            print('3. Quit')
            
            valid_choice = False
            while(valid_choice !=True):
                choice = input('Make your choice : ')
                if(choice == '1' or choice == '2' or choice == '3'):
                    valid_choice = True
                else:
                    print('Invalid choice.')
            
            if (choice == '1'):
                game.clear_grid()
            elif (choice == '2'):
                play_again = False
                game.clear_grid()
            else:
                play_again = False
                change_game_mode = False
                print('Bye !')

play_game()
