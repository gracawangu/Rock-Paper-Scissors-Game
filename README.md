# Rock-Paper-Scissors-Game

Rock-Paper-Scissors is a simple two-player game where, at a signal, players make moves with their hands, representing a rock, a piece of paper, or a pair of scissors.
The winner is determined according to a set of rules. If the two players make the same move, it’s a tie. On tne other hand, if the two players make different moves, Rock beats Scissors, Paper beats Rock and Scissors beats Paper.

# Game Program

The program is a simple version of the game with the two players being the User herein known as Player and the Computer herein known as CPU.
When the program is run, the User (Player) enters option "R" or "P" or "S" representing "Rock" or "Paper" or " Scissors". If input is invalid (not amongst the options), an error is printed and the User (Player) is asked to input again.
The`choice` function from the inbuilt Python `random` module is used to choose an option for the Computer (CPU). Both player's moves are printed in the format: `Player (Rock) : CPU (Paper)`.
If there is a winner (when the User (Player) and Computer (CPU) choose different options), the winner is printed and the program ends. If it's a tie (when the User (Player) and Computer (CPU) choose the same option), the game starts again.
