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
lst=[rock,paper,scissors]
random_value=random.randint(0,2)
user_value=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_value < 0 or user_value > 2:
    print("Invalid choice")
else:
 print(f"User choose: \n ")

 if user_value==0:
    print(rock)
 elif user_value==1:
    print(paper)
 else:
    print(scissors)


 print(f"Computer choose: \n {lst[random_value]}")

 if user_value==random_value:
    print("Its a tie")
 elif (user_value==0 and random_value==1)or(user_value==2 and random_value==0)or(user_value==1 and random_value==2):
    print("You lose")
 else :
    print("You win")



