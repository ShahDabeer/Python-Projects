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
users_choice=input("0 for rock,1 for paper,2 for scissors \n")
if users_choice=="0":
  print(rock)
elif users_choice=="1":
  print(paper)
elif users_choice=="2":
  print(scissors)

print("Computer Chose")
comp_chose = random.randint(0,2)
if comp_chose==0:
  print(rock)
elif comp_chose==1:
  print(paper)
elif comp_chose==2:
  print(scissors)

if users_choice=="0" and comp_chose==0:
    print("It is a tie")
elif users_choice=="0" and comp_chose==1:
    print("You won")
elif users_choice=="0" and comp_chose==2:
    print("You won")
elif users_choice=="1" and comp_chose==0:
    print("You lose")
elif users_choice=="1" and comp_chose==1:
    print("It is a tie")
elif users_choice=="1" and comp_chose==2:
    print("You lose")
elif users_choice=="2" and comp_chose==0:
    print("You won")
elif users_choice=="2" and comp_chose==1:
    print("You won")
elif users_choice=="2" and comp_chose==2:
    print("It is a tie")










