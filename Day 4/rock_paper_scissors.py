import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
player_choice = int(input("0 for rock, 1 for paper, 2 for scissors: "))
computer_choice = random.randint(0,2)

if player_choice == computer_choice:
    print(choices[player_choice] + "\nComputer chose:\n" + choices[computer_choice] + "\nTie!")
elif player_choice == 0 and computer_choice == 2:
    print(choices[player_choice] + "\nComputer chose:\n" + choices[computer_choice] + "\nYou win!")
elif player_choice == 1 and computer_choice == 0:
    print(choices[player_choice] + "\nComputer chose:\n" + choices[computer_choice] + "\nYou win!")
elif player_choice == 2 and computer_choice == 1:
    print(choices[player_choice] + "\nComputer chose:\n" + choices[computer_choice] + "\nYou win!")
else:
    print(choices[player_choice] + "\nComputer chose:\n" + choices[computer_choice] + "\nYou lose!")