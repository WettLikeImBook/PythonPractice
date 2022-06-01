# This is a rock, paper, scissors game
import random
import sys

# Print name of the game
print('ROCK, PAPER, SCISSORS')

# Keeping track of wins, losses, and ties
wins = 0
losses = 0
ties = 0

# Main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # Player Input Loop
        print('Enter your move: (R)ock, (P)aper, (S)cissors or (Q)uit')
        playerMove = input()
        if playerMove == 'Q':
            sys.exit()  # Quits the Program
        if playerMove == 'R' or 'P' or 'S':
            break  # Break out of the player input loop
        print('Type one of R, P, S, or Q')

    # Display what the player chose
    if playerMove == 'R':
        print('Rock versus...')
    elif playerMove == 'P':
        print('Paper versus...')
    elif playerMove == 'S':
        print('Scissors versus...')

    # Display what the computer chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'R'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'P'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 'S'
        print('SCISSORS')

    # Display win, lose or draw
    if playerMove == computerMove:
        print('Its a tie!')
        ties = ties + 1
    elif playerMove == 'R' and computerMove == 'S':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'R' and computerMove == 'P':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 'P' and computerMove == 'S':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 'P' and computerMove == 'R':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'S' and computerMove == 'P':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'S' and computerMove == 'R':
        print('You Lose!')
        losses = losses + 1
