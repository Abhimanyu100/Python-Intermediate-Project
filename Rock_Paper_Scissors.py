# importing 'random' module
from random import randint

player = input('rock (r), paper (p) or Scissors (s)? :') #print on the screen to choose between r(rock), paper(p),and scissors(s)

print(player, 'vs')

chosen = randint(1, 3)
print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print('computer has choosen ', computer)


print(player, 'vs', end=' ')

if player == computer: # if statement compare the both value of 'player' and 'computer'
    print('DRAW!')

elif player == 'r' and computer == 's':
    print('Player wins!')
elif player == 'r' and computer == 'p':
    print('Computer wins!')
elif player == 'p' and computer == 'r':
    print('Player wins!')
elif player == 'p' and computer == 's':
    print('Computer wins!')


