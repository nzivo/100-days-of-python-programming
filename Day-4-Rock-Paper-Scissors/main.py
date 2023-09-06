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

#Write your code below this line 👇

item_list = [rock, paper, scissors]

item_of_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(item_list[item_of_choice])

computer_choice = random.randint(0, 2)

print("Computer chose:")
print(item_list[computer_choice])

if item_of_choice >= 3 or item_of_choice < 0:
  print("You typed an invalid number, you lose!")
elif item_of_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and item_of_choice == 2:
  print("You lose")
elif computer_choice > item_of_choice:
  print("You lose")
elif item_of_choice > computer_choice:
  print("You win!")
elif computer_choice == item_of_choice:
  print("It's a draw")

