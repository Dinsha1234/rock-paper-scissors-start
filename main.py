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
import random
game_images=[rock,paper,scissors]
user_name=input("Welcome to Rock, Paper and Scissors.Please Enter your name")
print(f"Let's begin the war! {user_name} vs computer!!!")

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for paper, or 2 for scissors"))
if user_choose>=3 or user_choose<0:
  print("You typed an invalid number, you lose!!")
else:
  print(game_images[user_choose])

computer = random.randint(0,2)
print("Computer choose:")
print(game_images[computer])

if user_choose==computer:
  print("Tie!")
elif user_choose==0 and computer==1:
  print("Computer wins")
elif user_choose==0 and computer==2:
  print(f"Congratulations!!! {user_name} wins")
elif user_choose==1 and computer==0:
  print(f"Congratulations!!! {user_name} wins")
elif user_choose==1 and computer==2:
  print("Computer wins")
elif user_choose==2 and computer==0:
  print("Computer wins")
elif user_choose==2 and computer==1:
 print(f"Congratulations!! {user_name} wins")





