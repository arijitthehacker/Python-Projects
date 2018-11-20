#!/bin/python3
# A simple Rock Paper Scissors game. Using random Package. 

from random import randint

player=input("Choose Rock(r), Paper(p) or Scissors(s)")

print (player, ' vs ', end=' ')

chosen = randint(1,3)

# r = 1
# p = 2
# s = 3

if chosen == 1:
  computer = 'r'
elif chosen == 2:
  computer = 'p'
else:
  computer = 's'
  
print (computer)

'''If Player choses Rock & Computer choses Scissors: Winner Player
   If Player choses Paper & Computer choses Rock: Winner Player
   If Player choses Scissor & Computer choses Paper: Winner Player
   '''
   
if player == computer:
  print("Draw")
elif player == 'r' and computer == 's':
  print("Player Wins !!")
elif player == 'p' and computer == 'r':
  print("Player Wins !!")
elif player == 's' and computer == 'p':
  print("Player Wins !!")
# Let's give computer the chance to win
elif player == 'r' and computer == 'p':
  print("Computer Wins !!")
elif player == 'p' and computer == 's':
  print("Computer Wins !!")
elif player == 's' and computer == 'r':
  print("Computer Wins !!")
else:
  print("Error !! Wrong choice perhaps ?")
  
  
