# Rock-Paper-Scissors Game

print('Welcome to Rock-Paper-Scissors Game')

while True:
    print('\nStarting the Game\n')
    print('Game Options: ' 'Rock = R' ', ' 'Paper = P' ', ' 'Scissors = S')

    game_options = ['Rock','Paper','Scissors']
    player_option = input('Please enter R, P or S: ')
    
    if player_option == 'R':
        player_choice = 'Rock'
    elif player_option == 'P':
        player_choice = 'Paper'
    elif player_option == 'S':
        player_choice = 'Scissors'
    else:
        print('Invalid option, try again. Use capital letters')
        continue          

    if (player_choice in game_options):
        import random
        CPU_choice = random.choice(game_options)
        print('Player', ('('+player_choice+')'), ':', 'CPU', ('('+CPU_choice+')\n'))

    if player_choice == CPU_choice:
        print('It is a tie')
        continue
    elif player_choice == 'Rock'and CPU_choice == 'Scissors':
        print('Player Wins')
        break
    elif player_choice == 'Rock'and CPU_choice == 'Paper':
        print('CPU Wins')
        break
    elif player_choice == 'Paper'and CPU_choice == 'Rock':
        print('Player Wins')
        break
    elif player_choice == 'Paper'and CPU_choice == 'Scissors':
        print('CPU Wins')
        break
    elif player_choice == 'Scissors'and CPU_choice == 'Paper':
        print('Player Wins')
        break
    elif player_choice == 'Scissors'and CPU_choice == 'Rock':
        print('CPU Wins')
        break
