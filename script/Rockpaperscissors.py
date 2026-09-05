# Simple Rock-Paper-Scissors game using Python.
# The user selects Rock, Paper, or Scissors, the computer makes a random choice,
# and the program determines the winner based on the game rules.

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
scissors
'''
image =[rock,paper,scissors] #[0,1,2]

choice= int(input("What do you want to choose? 0 for  rock , 1 for paper, 2 for scissors: "))
if choice >= 0 and choice <=2:
    print(image[choice])
computer =random.randint(0,2)
print('Computer chose')
print(image[computer])

if choice <0 or choice > 2:
    print("Invalid choice")
elif choice== 0 and computer == 2 : ##far end comparision
    print("You win!")
elif choice == 2 and computer== 0: ##far end comparision
 print("You Lose!")
elif choice > computer:
    print("You Win!")
elif choice < computer:
    print("You Lose!")
elif choice==computer :
    print("Its a draw!")









